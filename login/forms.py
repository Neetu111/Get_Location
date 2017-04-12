from django import forms
from .models import *

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ('user_name', 'password',)

class detailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ('state','city', 'address',)