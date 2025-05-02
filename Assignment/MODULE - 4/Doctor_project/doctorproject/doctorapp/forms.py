from django import forms
from .models import *

class AppointmentForm(forms.ModelForm):
    class Meta :
        model = Appointmentinfo
        fields = '__all__'