from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=65, label='Номер телефона')

    password1 = forms.CharField(max_length=65, label='Пароль')
    password2 = forms.CharField(max_length=65, label='Подтверждение пароля')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, label='Номер телефона')
    password = forms.CharField(max_length=65, label='Имя')
