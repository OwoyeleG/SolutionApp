from dataclasses import fields
from django import forms
from .models import *

class ReportForm(forms.ModelForm):
    class Meta:
        model = SubUnitReport
        fields = '__all__'