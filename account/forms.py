from account.models import Account
from django import forms
from django.forms import TextInput




class AccountForm(forms.ModelForm):

    # class Meta:
    #     model = Account
    #     fields = "__all__"
    class Meta():
        model = Account
        fields = [ "type",'account_number',"amount","user" ]
        widgets = {
            'type':forms.Select(attrs={
                'class': "form-control"
            }),
            'account_number':TextInput(attrs={
                'class':'form-control'
            }),
            'amount':TextInput(attrs={
                'class':'form-control'
            }),
            'user':forms.Select(attrs={
                'class': "form-control"
            }),

        }