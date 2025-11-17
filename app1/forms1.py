from django import forms
from app1.models import employee
class update_employee_form(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'