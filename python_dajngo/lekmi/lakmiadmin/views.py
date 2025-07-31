from django.shortcuts import render

# Create your views here.

def add_category(reqeest):
    return render(reqeest,"add_category.html")

def add_product(reqeest):
    return render(reqeest,"add_product.html")

def admin_login(reqeest):
    return render(reqeest,"admin_login.html")

def admin_product(reqeest):
    return render(reqeest,"admin_product.html")

def Dashboard(reqeest):
    return render(reqeest,"Dashboard.html")

def Register_admin(reqeest):
    return render(reqeest,"Register_admin.html")