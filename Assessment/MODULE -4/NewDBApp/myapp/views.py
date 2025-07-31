from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.


def index(request):
    msg = ""
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record Inserted!")
            msg = "Record Inserted!"
            # return redirect("/")
        else:
            print(form.errors)
            msg = "Error!"
    return render(request, "index.html", {"msg": msg})


def showdata(request):
    stdata = userinfo.objects.all()
    return render(request, "showdata.html", {"stdata": stdata})


def deletedata(request, id):
    stid = userinfo.objects.get(id=id)
    userinfo.delete(stid)
    return redirect("showdata")


def updatedata(request, id):
    msg = ""
    stid = userinfo.objects.get(id=id)
    if request.method == "POST":
        update = updateuserForm(request.POST, instance=stid)
        if update.is_valid():
            update.save()
            print("Record Updated!")
            msg = "Record Updated!"
            return redirect("showdata")
        else:
            print(update.errors)
            msg = "Error!"
    return render(request, "updatedata.html", {"stid": stid})
