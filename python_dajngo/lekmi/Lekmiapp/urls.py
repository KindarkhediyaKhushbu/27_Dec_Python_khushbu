from django.contrib import admin
from django.urls import path, include
from Lekmiapp import views


urlpatterns = [
    path("", views.index),
    path("category/", views.category, name="category"),
    path("log_in/", views.log_in, name="log_in"),
    path("product/", views.product, name="product"),
    path("sign_up/", views.sign_up, name="sign_up"),
    
]