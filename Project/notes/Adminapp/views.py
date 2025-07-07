from django.shortcuts import render, redirect, get_object_or_404
from Noteapp.models import *
from datetime import datetime
from notes import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail


# Create your views here.


def admin_index(request):
    if request.method == "POST":
        username = "admin"
        password = "admin@123"

        unm = request.POST["username"]
        pas = request.POST["password"]

        if username == unm and password == pas:
            print("Login Successfully!")
            return redirect("admin_home")
        else:
            print("Error!Login faild...")
    return render(request, "admin_index.html")


def admin_home(request):
    return render(request, "admin_home.html")


def admin_userinfo(request):
    userdata = Usersignup.objects.all()
    return render(request, "admin_userinfo.html", {"userdata": userdata})


def admin_notesinfo(request):
    notesdata = Notes.objects.all()
    return render(request, "admin_notesinfo.html", {"notesdata": notesdata})


def notes_approve(request, id):
    notes = get_object_or_404(Notes, id=id)
    notes.status = "Approved"
    notes.updated_at = datetime.now()
    notes.save()

    # Email Sending
    subject = "🎉 Your Notes Have Been Approved!"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [notes.username.username]

    context = {
        "user_name": notes.username.firstname,
        "notes_title": notes.title,
    }

    # Load and render HTML template
    html_message = render_to_string("emails/approve_mail.html", context)
    plain_message = f"""
    Hello {notes.username.firstname},

    Your notes titled "{notes.title}" have been approved by the admin.

    Thank you!
    TOPS Technologies
    """

    try:
        send_mail(
            subject,
            plain_message,  # Plain text message (fallback)
            from_email,
            recipient_list,
            fail_silently=False,
            html_message=html_message,  # HTML message for modern email clients
        )
        print("Approval email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
    print("Email Sent successfully!")
    print("Your notes has been approved!")
    return redirect("admin_notesinfo")


def notes_reject(request, id):
    notes = get_object_or_404(Notes, id=id)
    notes.status = "Rejected"
    notes.updated_at = datetime.now()
    notes.save()
    print("Your notes has been rejected!")
    return redirect("admin_notesinfo")