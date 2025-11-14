from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import MySuperUser

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Логін"
    )

    first_name = forms.CharField(
        label="Ім'я",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    last_name = forms.CharField(
        label="Прізвище",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=20
    )

    email = forms.EmailField(
        max_length=250,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        label="Електронна пошта"
    )

    phone_number = forms.CharField(
        label="Номер телефону",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=16,
        required=False
    )

    address = forms.CharField(
        label="Адреса",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=200,
        required=False
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        max_length=100
    )

    password2 = forms.CharField(
        label="Повторіть пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        max_length=100
    )

    class Meta:
        # model = User
        model = MySuperUser
        fields = ("username", "first_name", "last_name", "email", "phone_number", "address", "password1", "password2")

    class LoginForm(AuthenticationForm):
        username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}), label="Логін")
        password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}), label="Пароль")