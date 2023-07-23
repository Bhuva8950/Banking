from django.contrib import admin
from django.urls import path
from account.views import Home, AccountListView, AccountCreateView, AccountUpdateView,AccountDetailView,AccountDeleteView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("account-list/", AccountListView.as_view(), name="account_list"),
    path("account-create/", AccountCreateView.as_view(), name="account_create"),
    path("<int:pk>/update/", AccountUpdateView.as_view(), name="account_update"),
    path("<int:pk>/details/", AccountDetailView.as_view(), name="account_details"),
    path("<int:pk>/delete/", AccountDeleteView.as_view(), name="account_delete"),
]