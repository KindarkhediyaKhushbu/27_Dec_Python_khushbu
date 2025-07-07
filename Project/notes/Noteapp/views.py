from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.mail import send_mail
import random
from notes import settings
from django.contrib.auth import logout


# Create your views here.
def index(request):
    user = request.session.get("user")
    return render(request, "index.html", {"user": user})


def notes(request):
    msg =''
    user = request.session.get("user")
    if request.method == "POST":
        username = Usersignup.objects.get(username=user)
        print("Username:", username)
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            cuser = form.save(commit=False)
            cuser.status = "Pending"
            cuser.username = username
            cuser.save()
            print("Your notes has been submitted!")
            msg = 'Your notes has been submitted'
        else:
            print(form.errors)
    return render(request, "notes.html", {"user": user,'msg':msg})


def profile(request):
    msg = ""
    user = request.session.get("user")
    userid = request.session.get("userid")
    cuser = Usersignup.objects.get(id=userid)
    if request.method == "POST":
        form = UpdateForm(request.POST, request.FILES, instance=cuser)
        if form.is_valid():
            form.save()
            print("Profile updated!")
            return redirect("profile")
        else:
            print(form.errors)
            msg = "Error! Something went wrong..."
    return render(request, "profile.html", {"user": user, "cuser": cuser, "msg": msg})


def about(request):
    user = request.session.get("user")
    return render(request, "about.html", {"user": user})


def contact(request):
    user = request.session.get("user")
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Your message has been sent!")
        else:
            print(form.errors)
    return render(request, "contact.html", {"user": user})


def login(request):
    user = request.session.get("user")
    msg = ""
    if request.method == "POST":
        unm = request.POST["username"]
        pas = request.POST["password"]
        user = Usersignup.objects.filter(username=unm, password=pas)
        userid = Usersignup.objects.get(username=unm)
        print("Current UserID:", userid.id)
        if user:  # TRUE
            print("Login Successfull!")
            request.session["user"] = unm  # generate a session
            request.session["userid"] = userid.id
            return redirect("notes")
        else:
            print("Error! Something went wrong..")
            msg = "Error! Something went wrong.."
    return render(request, "login.html", {"msg": msg, "user": user})


def signup(request):
    user = request.session.get("user")
    msg = ""
    if request.method == "POST":
        form = UsersignupForm(request.POST, request.FILES)
        username = ""
        if form.is_valid():
            username = form.cleaned_data.get("username")
            try:
                Usersignup.objects.get(username=username)
                print("Username is already exists!")
                msg = "Username is already exists!"
            except Usersignup.DoesNotExist:
                form.save()
                print("Signup successfully!")
                msg = "Signup Successfully!"

                # Email Sending Code
                global otp
                otp = random.randint(11111, 99999)
                send_mail(
                    subject="Your OTP Verification",
                    message=f"Dear User!\n\nThank you for registration with us!\nYour one time password is {otp}\n\nThanks & Regards!\nNotesApp\nTOPS Technologies\n+9724799469 | sanket.tops@gmail.com",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[request.POST["username"]],
                )
                return redirect("otpverify")
        else:
            print(form.errors)
    return render(request, "signup.html", {"msg": msg, "user": user})


def otpverify(request):
    user = request.session.get("user")
    msg = ""
    print("OTP:", otp)
    if request.method == "POST":
        if request.POST["otp"] == str(otp):
            print("Verification success!")
            return redirect("login")
        else:
            print("Error!Verification faild...Plz try again")
            msg = "Error!Verification faild...Plz try again"
    return render(request, "otpverify.html", {"msg": msg, "user": user})


def userlogout(request):
    logout(request)
    return redirect("/")