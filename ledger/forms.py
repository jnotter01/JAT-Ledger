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