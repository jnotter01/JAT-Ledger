from django.contrib import admin
from .models import Property, Category, Transaction


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state", "active", "created_at")
    list_filter = ("active", "state")
    search_fields = ("name", "address", "city")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category_type", "user")
    list_filter = ("category_type",)
    search_fields = ("name",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "transaction_type",
        "amount",
        "property",
        "category",
        "transaction_date",
        "user",
    )
    list_filter = ("transaction_type", "transaction_date")
    search_fields = ("description", "property__name", "category__name")