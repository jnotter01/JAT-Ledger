from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path("properties/", views.property_list, name="property_list"),
    path("properties/create/", views.property_create, name="property_create"),

    path("transactions/", views.transaction_list, name="transaction_list"),
    path("transactions/create/", views.transaction_create, name="transaction_create"),
    path("reports/summary/", views.report_summary, name="report_summary"),

    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.category_create, name="category_create"),
]