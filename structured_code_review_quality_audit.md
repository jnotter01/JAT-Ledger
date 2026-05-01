# Structured Code Review & Quality Audit

## Part 1: Code Selection

### Feature Name

Transaction Management and Summary Reporting

### Feature Description

The feature selected for this structured self-review is the transaction management and summary reporting portion of JAT Ledger. This feature allows the user to create income and expense records, connect each transaction to a rental property and category, display saved transactions, and calculate basic financial totals such as total income, total expenses, and net profit.

This is meaningful functionality because it is one of the core purposes of the application. JAT Ledger is not only storing records; it also needs to validate financial data, protect user-owned records, and calculate accurate summaries for rental property decision-making. Because this feature affects the reliability of the ledger, it was reviewed before moving further into implementation.

### Files Reviewed

The following files were reviewed:

```text
ledger/models.py
ledger/forms.py
ledger/views.py
ledger/services.py
ledger/urls.py
ledger/templates/ledger/base.html
ledger/templates/ledger/transaction_list.html
ledger/templates/ledger/transaction_form.html
ledger/templates/ledger/report_summary.html
jatledger/urls.py
```

### Approximate Lines of Code

Approximately 250 lines of code were reviewed across the models, forms, views, service logic, URL routing, and templates.

---

## Part 2: Structured Code Review

Because this is a solo capstone project, this review was completed as a formal structured self-review. The reviewed feature was checked for correctness, architecture alignment, readability, security, validation, and performance.

---

## A. Correctness

### Strength

The transaction feature meets the main requirements for the first working version of the ledger. A user can create a transaction, connect it to a property and category, view the transaction in a list, and see the transaction reflected in the summary report. The `Transaction` model also includes important fields such as user, property, category, transaction type, amount, description, and transaction date.

### Improvement Suggestion

The first version needed stronger validation for transaction amounts. A transaction amount should not be allowed to be zero or negative because that would create incorrect financial records. This issue was selected for refactoring by adding validation to `TransactionForm`.

---

## B. Architecture Alignment

### Strength

The code mostly follows the system architecture plan. The project separates database structure into `models.py`, form handling into `forms.py`, request handling into `views.py`, URL routing into `urls.py`, and display into templates. This supports a clean Django project structure.

### Improvement Suggestion

The first version placed report calculation logic directly inside `views.py`. This made the view responsible for both request handling and business logic. To better match the architecture plan, the financial summary calculation was moved into `services.py`.

---

## C. Readability & Maintainability

### Strength

The code uses clear names that describe the purpose of each part of the feature. Names such as `Property`, `Category`, `Transaction`, `TransactionForm`, `transaction_list`, `transaction_create`, and `report_summary` are easy to understand. The templates are also separated by purpose, which makes the feature easier to maintain.

### Improvement Suggestion

Some logic could become duplicated as the project grows. For example, filtering transactions by the logged-in user may be needed in multiple views. Future improvements should consider helper functions or consistent query patterns to reduce repeated code and lower the chance of security mistakes.

---

## D. Security & Validation

### Strength

The views use Django’s `login_required` decorator, which helps prevent unauthenticated users from accessing transaction and report pages. Transactions are also filtered by `request.user`, which helps protect user-owned financial records.

### Improvement Suggestion

All user-owned queries should continue to filter by `request.user`. If future edit or delete views are added, they should not retrieve transactions by ID alone. They should check both the transaction ID and the logged-in user to prevent one user from accessing another user’s records.

---

## E. Performance Considerations

### Strength

The current feature is appropriate for the expected project size. The application is designed for a small rental business, so simple database queries and report calculations are acceptable for the first version.

### Improvement Suggestion

The current summary calculation loops through the user’s transactions in Python. This works for a small number of records, but if the number of transactions grows, Django aggregate queries may be more efficient. Future versions could use database-level aggregation for income and expense totals.

---

## Improvement Opportunities Identified

The review identified the following improvement opportunities:

1. Move financial summary calculations out of `views.py` and into `services.py`.
2. Add validation to prevent zero or negative transaction amounts.
3. Make sure user-owned records are always filtered by the logged-in user.
4. Avoid duplicated validation messages between forms and models.
5. Consider database aggregation for reports if transaction volume grows.
6. Improve user-facing form error styling in the templates.
7. Add automated tests for summary calculations and form validation.

---

## Refactor 1: Move Report Calculations into `services.py`

### Issue Found

The first version of `report_summary` placed financial calculation logic directly in `views.py`. This made the view responsible for too many tasks: retrieving transactions, calculating totals, and rendering the template.

### Before Code

```python
from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import TransactionForm
from .models import Transaction


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
```

### After Code

```python
# ledger/services.py

from decimal import Decimal


def calculate_summary(transactions):
    total_income = Decimal("0.00")
    total_expenses = Decimal("0.00")

    for transaction in transactions:
        if transaction.transaction_type == "Income":
            total_income += transaction.amount
        elif transaction.transaction_type == "Expense":
            total_expenses += transaction.amount

    net_profit = total_income - total_expenses

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_profit": net_profit,
    }
```

```python
# ledger/views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import TransactionForm
from .models import Transaction
from .services import calculate_summary


@login_required
def report_summary(request):
    transactions = Transaction.objects.filter(user=request.user)
    summary = calculate_summary(transactions)

    return render(request, "ledger/report_summary.html", summary)
```

### Explanation of Improvement

This refactor improves separation of concerns. The view now handles the request and response, while `services.py` handles the business logic for financial calculations. This makes the summary calculation easier to test, easier to reuse, and easier to change later.

---

## Refactor 2: Add Transaction Amount Validation

### Issue Found

The first version of `TransactionForm` did not include form-level validation to reject zero or negative transaction amounts. This could allow invalid financial records to be submitted through the form.

### Before Code

```python
from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "property",
            "category",
            "transaction_type",
            "amount",
            "description",
            "transaction_date",
        ]

        widgets = {
            "transaction_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 3}),
        }
```

### After Code

```python
from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "property",
            "category",
            "transaction_type",
            "amount",
            "description",
            "transaction_date",
        ]

        widgets = {
            "transaction_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 3}),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get("amount")

        if amount is None:
            raise forms.ValidationError("Amount is required.")

        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")

        return amount
```

### Explanation of Improvement

This refactor improves correctness and validation. The form now rejects missing, zero, or negative transaction amounts before the transaction is saved. This helps protect the accuracy of reports and prevents invalid financial data from entering the ledger.

---

## Additional Review Finding: Duplicate Validation Message

### Issue Found

While testing the form validation, the message `Transaction type must match the selected category type` appeared twice. This happened because the same validation rule was being checked in more than one place.

### Resolution

The duplicate form-level category/type validation was removed from `TransactionForm`, while the model-level validation remained in `Transaction.clean()`. This keeps the important rule in the model and avoids showing duplicate error messages to the user.

### Code Kept in `models.py`

```python
def clean(self):
    if self.amount is not None and self.amount <= 0:
        raise ValidationError("Transaction amount must be greater than zero.")

    if self.category and self.transaction_type:
        if self.category.category_type != self.transaction_type:
            raise ValidationError("Transaction type must match the selected category type.")
```

### Explanation of Improvement

This improves maintainability and user experience. The validation rule is still enforced, but the user no longer sees the same error message twice.

---

## Instructor Feedback Request

I would like instructor feedback on the separation between `views.py` and `services.py`. Specifically, I would like to know whether moving the report calculation logic into `services.py` is the best structure for this project, or whether another approach would be better as the project grows.

---

## Part 3: Reflection

### What issues were discovered during the review?

The review discovered that the first working version had report calculation logic inside `views.py`, which did not fully match the planned architecture. It also showed that transaction amount validation needed to be stronger, because zero or negative amounts should not be accepted. During validation testing, a duplicate validation message was also discovered and corrected.

### Were any architectural inconsistencies identified?

Yes. The main architectural inconsistency was that business logic was originally placed directly inside the `report_summary` view. The architecture plan separates request handling from business logic, so this was corrected by moving the calculation logic into `services.py`.

### What would have happened if this code were merged without review?

If the code were merged without review, the application would still work at a basic level, but it would be harder to maintain and test. Invalid transaction amounts could affect reports, and business logic inside views could become messy as more reports are added. The duplicate validation message could also confuse users when they submit invalid forms.

### How will you integrate code reviews into future sprints?

For future sprints, code review will be included before finalizing each major feature. Since this is a solo project, I will use a structured self-review checklist covering correctness, architecture alignment, readability, security, validation, and performance. I will also use GitHub commits and GitHub Issues to track problems found during review and confirm that fixes have been completed.
