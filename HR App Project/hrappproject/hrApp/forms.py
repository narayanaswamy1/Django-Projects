from django import forms
from hrApp.models import EmployeeDatabaseForm
from django.forms.widgets import DateInput

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeDatabaseForm
        fields = '__all__'
        widgets = {
            'dateOfBirth': DateInput(attrs={'type': 'date'})
        }
