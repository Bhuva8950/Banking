from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255, null=True, blank=True)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255)

    def __str__(self) :
        return self.first_name

class Employees(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255, null=True, blank=True)
    age = models.PositiveIntegerField()
    date_of_joining = models.DateField()

    def __str__(self) :
        return self.first_name

class Account(models.Model):
    SAVING = "saving"
    SALARY = "salary"

    account_type = (
        (SALARY, SALARY),
        (SAVING, SAVING)
    )
    type = models.CharField(max_length=255, choices=account_type, default=SAVING)
    account_number = models.PositiveIntegerField()
    amount = models.IntegerField(default=0)
    user = models.ForeignKey(Customer, related_name="account_user", on_delete=models.CASCADE)

    def __str__(self) :
        return f"{self.user} - {self.account_number}"