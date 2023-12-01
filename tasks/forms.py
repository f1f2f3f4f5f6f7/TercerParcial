from django.forms import ModelForm
from .models import Notas
from django import forms

class NotasForm(ModelForm):
    class Meta:
        model= Notas
        fields = ['title', 'nota']
        widgets = {
            'datecompleted': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
