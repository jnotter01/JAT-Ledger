from .services import calculate_summary

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import CategoryForm, PropertyForm, TransactionForm
from .models import Category, Property, Transaction
from .services import calculate_summary

@login_required
def dashboard(request):
    transaction_count = Transaction.objects.filter(user=request.user).count()
    recent_transactions = Transaction.objects.filter(user=request.user).order_by("-transaction_date")[:5]

    return render(request, "ledger/dashboard.html", {
        "transaction_count": transaction_count,
        "recent_transactions": recent_transactions,
    })

@login_required
def property_list(request):
    properties = Property.objects.filter(user=request.user).order_by("name")

    return render(request, "ledger/property_list.html", {
        "properties": properties,
    })


@login_required
def property_create(request):
    if request.method == "POST":
        form = PropertyForm(request.POST)

        if form.is_valid():
            property_record = form.save(commit=False)
            property_record.user = request.user
            property_record.save()
            return redirect("property_list")
    else:
        form = PropertyForm()

    return render(request, "ledger/property_form.html", {
        "form": form,
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

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user).order_by("category_type", "name")

    return render(request, "ledger/category_list.html", {
        "categories": categories,
    })

@login_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect("category_list")
    else:
        form = CategoryForm()

    return render(request, "ledger/category_form.html", {
        "form": form,
    })

@login_required
def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST, user=request.user)

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm(user=request.user)

    return render(request, "ledger/transaction_form.html", {
        "form": form,
    })