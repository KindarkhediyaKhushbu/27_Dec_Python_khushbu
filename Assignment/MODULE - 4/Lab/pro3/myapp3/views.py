from django.shortcuts import render
from .forms import *

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data (for example, save it or send an email)
            print(form.cleaned_data)  # For demo purposes, we are just printing it.
            return render(request, 'formapp/success.html')
    else:
        form = ContactForm()

    return render(request, 'formapp/contact.html', {'form': form})
