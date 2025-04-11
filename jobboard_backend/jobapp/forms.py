from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title',
            'category',
            'company_email',
            'description',
            'company_location',
            'position_salary',
            'position_location',
            'company_name',
        ]
