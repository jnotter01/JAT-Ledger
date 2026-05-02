from datetime import date
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .forms import TransactionForm
from .models import Category, Property, Transaction
from .services import calculate_summary


class SummaryServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPass123"
        )

        self.property = Property.objects.create(
            user=self.user,
            name="Test Property",
            address="123 Test Street",
            city="Quahog",
            state="RI",
            zip_code="02860",
        )

        self.rent_category = Category.objects.create(
            user=self.user,
            name="Rent",
            category_type="Income",
        )

        self.repair_category = Category.objects.create(
            user=self.user,
            name="Repairs",
            category_type="Expense",
        )

    def test_calculate_summary_with_income_and_expenses(self):
        Transaction.objects.create(
            user=self.user,
            property=self.property,
            category=self.rent_category,
            transaction_type="Income",
            amount=Decimal("1000.00"),
            description="Rent payment",
            transaction_date=date.today(),
        )

        Transaction.objects.create(
            user=self.user,
            property=self.property,
            category=self.repair_category,
            transaction_type="Expense",
            amount=Decimal("250.00"),
            description="Repair cost",
            transaction_date=date.today(),
        )

        summary = calculate_summary(Transaction.objects.filter(user=self.user))

        self.assertEqual(summary["total_income"], Decimal("1000.00"))
        self.assertEqual(summary["total_expenses"], Decimal("250.00"))
        self.assertEqual(summary["net_profit"], Decimal("750.00"))

    def test_calculate_summary_with_no_transactions(self):
        summary = calculate_summary(Transaction.objects.none())

        self.assertEqual(summary["total_income"], Decimal("0.00"))
        self.assertEqual(summary["total_expenses"], Decimal("0.00"))
        self.assertEqual(summary["net_profit"], Decimal("0.00"))


class TransactionFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="formuser",
            password="TestPass123"
        )

        self.property = Property.objects.create(
            user=self.user,
            name="Form Property",
            address="456 Form Street",
            city="Quahog",
            state="RI",
            zip_code="02860",
        )

        self.rent_category = Category.objects.create(
            user=self.user,
            name="Rent",
            category_type="Income",
        )

    def test_transaction_form_rejects_zero_amount(self):
        form = TransactionForm(
            data={
                "property": self.property.id,
                "category": self.rent_category.id,
                "transaction_type": "Income",
                "amount": "0",
                "description": "Invalid amount",
                "transaction_date": date.today(),
            },
            user=self.user,
        )

        self.assertFalse(form.is_valid())
        self.assertIn("amount", form.errors)

    def test_transaction_form_accepts_valid_amount(self):
        form = TransactionForm(
            data={
                "property": self.property.id,
                "category": self.rent_category.id,
                "transaction_type": "Income",
                "amount": "100.00",
                "description": "Valid amount",
                "transaction_date": date.today(),
            },
            user=self.user,
        )

        self.assertTrue(form.is_valid())


class ViewAccessTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="viewuser",
            password="TestPass123"
        )

    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response.url)

    def test_transaction_setup_guard_for_new_user(self):
        self.client.login(username="viewuser", password="TestPass123")

        response = self.client.get(reverse("transaction_create"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Setup Required")
        self.assertContains(response, "Property setup")
        self.assertContains(response, "Category setup")