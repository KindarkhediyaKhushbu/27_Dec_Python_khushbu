from django.shortcuts import render

# Create your views here.
def home(request):
    message ="Fisrt Django Website"
    return render(request,'home.html',{"message":message})
