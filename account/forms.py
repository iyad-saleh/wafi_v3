from django import forms
from .models import Account_type, Main_account, Sub_account



# class AccountForm(forms.ModelForm):
#     name = forms.CharField(widget=forms.TextInput(attrs={"tabindex":"0"}))

#     class Meta:
#         model = Account
#         fields = ['name','account_type' ]


class Account_typeForm(forms.ModelForm):
    class Meta:
        model = Account_type
        fields = ['code','name','nature','final','ar_name']

class Main_accountForm(forms.ModelForm):
    class Meta:
        model = Main_account
        fields = ['code','name','parent','ar_name'] #'account_type',

class Sub_accountForm(forms.ModelForm):
    class Meta:
        model = Sub_account
        fields = ['code','name','coin','ar_name']#'main_account',
