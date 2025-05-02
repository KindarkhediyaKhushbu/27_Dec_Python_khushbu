from django.contrib import admin
from django.urls import path,include
from doctorapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about,name='about'),
    path('appointment/',views.appointment,name='appointment'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('detail/',views.detail,name='detail'),
    path('price/',views.price,name='price'),
    path('search/',views.search,name='search'),
    path('service/',views.price,name='price'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimonial'),
]
                        