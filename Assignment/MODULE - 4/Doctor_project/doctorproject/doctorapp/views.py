from django.shortcuts import render,redirect
from .forms import *
from .models import *

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def appointment(request):
    msg=''
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            print('Appiontment Done!')
            msg="Your Appointment Has Been Submited!"
            return redirect('/')
        else:
            print(form.errors)
            msg="Error! Something went Wrong...!"
    return render(request, 'appointment.html',{'msg':msg})

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

def doctor_profile(request):
    msg=""
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("data inserted") 
            msg="Record Inserted Successfully!"      
            return redirect('/')
    else:
        form = DoctorProfileForm()
        msg="Error! Something went Wrong...! Try Again "
    return render(request, 'doctor_profile.html', {'form': form,'msg':msg})

def login(request):
    msg=''
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = patientregister.objects.filter(email=email,password=password)
        if user:
            print("Login Successfully")
            msg="Login Successfully!"
            return redirect('/')
        else:
            print("Error")
            msg="Oops! Login Faild..."
    return render(request,'login.html',{'msg':msg})
   

def register(request):
    msg=""
    if request.method == 'POST':
        form = patientForm(request.POST)
        if form.is_valid():
            form.save()
            print("Register successfully")
            msg="Registration Successfully!"
            return redirect('login')
        else:
            print(form.errors)
            msg="Oops! Something went wrong...!"
        
    return render(request,'register.html',{'msg':msg})
    