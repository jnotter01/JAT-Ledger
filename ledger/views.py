from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import TransactionForm
from .models import Transaction


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

    total_income = Decimal("0.00")
    total_expenses = Decimal("0.00")

    for transaction in transactions:
        if transaction.transaction_type == "Income":
            total_income += transaction.amount
        elif transaction.transaction_type == "Expense":
            total_expenses += transaction.amount

    net_profit = total_income - total_expenses

    return render(request, "ledger/report_summary.html", {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_profit": net_profit,
    })