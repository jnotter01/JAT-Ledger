from .services import calculate_summary

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import TransactionForm
from .models import Transaction

@login_required
def dashboard(request):
    transaction_count = Transaction.objects.filter(user=request.user).count()
    recent_transactions = Transaction.objects.filter(user=request.user).order_by("-transaction_date")[:5]

    return render(request, "ledger/dashboard.html", {
        "transaction_count": transaction_count,
        "recent_transactions": recent_transactions,
    })

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by("-transaction_date")

    return render(request, "ledger/transaction_list.html", {
        "transactions": transactions,
    })


@login_required
def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm()

    return render(request, "ledger/transaction_form.html", {
        "form": form,
    })


@login_required
def report_summary(request):
    transactions = Transaction.objects.filter(user=request.user)
    summary = calculate_summary(transactions)

    return render(request, "ledger/report_summary.html", summary)