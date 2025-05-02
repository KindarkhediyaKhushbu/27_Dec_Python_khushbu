from django.contrib import admin
from .models import*

# Register your models here.
class doctorData(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id','first_name','last_name','specialty','phone_no','email','image','degree','bio']
    
    
admin.site.register(doctors,doctorData)