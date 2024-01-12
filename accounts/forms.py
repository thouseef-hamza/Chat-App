from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)


class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'role', 'password',)
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'role': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'password': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name','role',)
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'role': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }