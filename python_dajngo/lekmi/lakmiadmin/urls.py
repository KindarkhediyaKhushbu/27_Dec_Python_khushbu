from django.contrib import admin
from django.urls import path, include
from lakmiadmin import views


urlpatterns = [
    path("", views.add_category, name="add_category"),
    path("add_product/", views.add_product, name="add_product"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("admin_product/", views.admin_product, name="notes_approve"),
    path("Dashboard/", views.Dashboard, name="Dashboard"),
    path("Register_admin/",views.Register_admin, name="Register_admin ")
]