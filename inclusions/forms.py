from django import forms
from inclusions.models import Patient, Pathology


class NewPatient(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }


class NewPathology(forms.ModelForm):
    class Meta:
        model = Pathology
        fields = ['name']

"""
class NewInclusion(forms.ModelForm):
    class Meta:
        model = Inclusion
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
     }

"""