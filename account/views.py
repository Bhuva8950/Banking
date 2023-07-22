from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from account.models import Account, Customer, Employees
from django.urls import reverse_lazy
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
    fields = ("amount","account_number")


class AccountFormView(FormView):
    template_name = "account_form.html"
    form_class = AccountForm
    success_url = "/"