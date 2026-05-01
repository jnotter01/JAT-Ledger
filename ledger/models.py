from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError


class Property(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"


class Category(models.Model):
    INCOME = "Income"
    EXPENSE = "Expense"

    CATEGORY_TYPE_CHOICES = [
        (INCOME, "Income"),
        (EXPENSE, "Expense"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category_type = models.CharField(max_length=10, choices=CATEGORY_TYPE_CHOICES)

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ("user", "name", "category_type")

    def __str__(self):
        return f"{self.name} ({self.category_type})"


class Transaction(models.Model):
    INCOME = "Income"
    EXPENSE = "Expense"

    TRANSACTION_TYPE_CHOICES = [
        (INCOME, "Income"),
        (EXPENSE, "Expense"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    transaction_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.amount is not None and self.amount <= 0:
            raise ValidationError("Transaction amount must be greater than zero.")

        if self.category and self.transaction_type:
            if self.category.category_type != self.transaction_type:
                raise ValidationError("Transaction type must match the selected category type.")

    def __str__(self):
        return f"{self.transaction_type}: ${self.amount} on {self.transaction_date}"