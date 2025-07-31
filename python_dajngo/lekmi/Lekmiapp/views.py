from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request,"index.html")

def category(request):
    return render(request,"category.html")

def log_in(request):
    return render(request,"log_in.html")

def product(request):
    return render(request,"product.html")

def sign_up(request):
    return render(request, 'sign_up.html')

