from django import forms
from .models import Problem


class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        exclude = ['created_by', 'date_created', 'adopted', 'attempted', 'answered']
