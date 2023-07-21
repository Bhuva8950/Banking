from django.contrib import admin
from account.models import Account, Customer, Employees
# Register your models here.


admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Employees)