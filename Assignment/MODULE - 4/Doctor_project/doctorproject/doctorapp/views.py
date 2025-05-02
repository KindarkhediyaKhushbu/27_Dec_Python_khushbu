from django.shortcuts import render,redirect
from .forms import *

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            print('Appiontment Done!')
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'appointment.html',)

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def detail(request):
    return render(request,'detail.html')

def price(request):
    return render(request,'price.html')

def search(request):
    return render(request,'search.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')
