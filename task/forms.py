from django import forms
from django.forms import ModelForm

from .models import Task

class TaskForm(forms.ModelForm):
    
    tittle = forms.CharField()

    class Meta:
        model = Task
        fields = ['tittle', 'complete']