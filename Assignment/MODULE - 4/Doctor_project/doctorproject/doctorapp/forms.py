from django import forms
from .models import *

class AppointmentForm(forms.ModelForm):
    class Meta :
        model = Appointmentinfo
        fields = '__all__'
        
class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = '__all__'


class patientForm(forms.ModelForm):
    class Meta:
        model = patientregister
        fields = '__all__'