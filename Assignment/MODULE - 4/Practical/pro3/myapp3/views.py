from django.shortcuts import render

# Create your views here.
from .forms import PatientForm

def patient_registration(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page after submission
    else:
        form = PatientForm()
    return render(request, 'registration/patient_form.html', {'form': form})

def success(request):
    return render(request, 'registration/success.html')
