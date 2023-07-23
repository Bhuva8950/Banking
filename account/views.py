from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from account.models import Account, Customer, Employees
from django.urls import reverse_lazy, reverse
from account.forms import AccountForm

# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs) :
        return render(request, "welcome.html")

class AccountListView(ListView):
    model = Account
    template_name = "account.html"
    context_object_name = "account"

class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = "account_form.html"

    
    def get_success_url(self):
        return reverse("account_list")

class AccountUpdateView(UpdateView):
    model = Account
    template_name = "account_form.html"
    form_class = AccountForm

    def get_success_url(self):
        return reverse("account_list")


class AccountDetailView(DetailView):
    model = Account
    template_name = "account_detail.html"
    context_object_name = "account"

class AccountDeleteView(DeleteView):
    model = Account
    template_name = "account_delete.html"
    context_object_name = "account"
    
    def get_success_url(self):
        return reverse("account_list")