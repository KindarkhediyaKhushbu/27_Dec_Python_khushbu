from django.db import models

# Create your models here.
class Appointmentinfo(models.Model):
    DEPARTMENT_CHOICE = [
       ('Cardiologist','Cardiologist'),
       ('Neurologist','Neurologist'),
       ('Obstetrician-gynecologist','Obstetrician-gynecologist'),
       ('Psychiatrist','Psychiatrist'),
       ('Urologist','Urologist'),
       ('Family physician','Family physician'),
       ('Dentist','Dentist'),
       ('Geriatrician','Geriatrician'),
    ]
    
    DOCTOR_CHOICE = [
       ('Dr.Vinita sing','Dr.Vinita sing'),
       ('Dr.Ashu Sharma','Dr.Ashu Sharma'),
       ('Dr.Mukesh Kumar','Dr.Mukesh Kumar'),
       ('Dr.Sudhdha sharma','Dr.Sudhdha sharma'),
       ('Dr. Manish Jain','Dr. Manish Jain'),
       ('Dr.Rachana Gupta','Dr.Rachana Gupta'),
       ('Dr.Kuldeep Rajput ','Dr.Kuldeep Rajput'),
       ('Dr.Janvi Kindarkhediya','Dr.Janvi Kindarkhediya'),
    ]
    
    department = models.CharField(max_length=100,choices=DEPARTMENT_CHOICE)
    doctor = models.CharField(max_length=100,choices=DOCTOR_CHOICE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    
    
    from django.db import models

class DoctorProfile(models.Model):
    name = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    degree = models.CharField(max_length=100)
    bio = models.TextField()
    address = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.name

    
class patientregister(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    full_name = models.CharField(max_length=50)
    age = models.BigIntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    phone = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.TextField()