from account.models import Account
from django import forms



class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = "__all__"