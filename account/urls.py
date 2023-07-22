from django.contrib import admin
from django.urls import path
from account.views import Home, AccountListView, AccountFormView, AccountCreateView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("account-list/", AccountListView.as_view(), name="account_list"),
    path("account-create/", AccountCreateView.as_view(), name="account_create"),
    path("account-form/", AccountFormView.as_view(), name="account_form"),
]