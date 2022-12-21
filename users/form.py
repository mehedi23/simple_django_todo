from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from .models import CustomUser

class Sign_Up_form(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)