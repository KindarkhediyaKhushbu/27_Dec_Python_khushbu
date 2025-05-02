from django import forms
from .models import *

class patientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = '__all__'