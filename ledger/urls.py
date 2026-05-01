from django.urls import path

from . import views

urlpatterns = [
    path("transactions/", views.transaction_list, name="transaction_list"),
    path("transactions/create/", views.transaction_create, name="transaction_create"),
    path("reports/summary/", views.report_summary, name="report_summary"),
]