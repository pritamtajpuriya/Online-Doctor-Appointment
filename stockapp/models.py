from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db import models 
import datetime

class Contact(models.Model):
    name=models.CharField(max_length=250)
    number=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    message=models.TextField()

    def __str__(self):
        return self.number
        
class Category(models.Model):
    cat_name=models.CharField(max_length=250)
    cat_img=models.FileField(upload_to="media")
    cat_desc=models.TextField(max_length=250)

    def __str__(self):
        return self.cat_name


class Admin_Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile=models.ImageField(upload_to="media")
    contact_number=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    occupation=models.TextField(max_length=250)
    added_on=models.DateTimeField(auto_now=True)
    update_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
ch=(
    ("Male","Male"),("Female","Female"),("other","other")
    )
class Patient_Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=250,null=True)
    last_name=models.CharField(max_length=250,null=True)
    profile=models.ImageField(upload_to="media")
    contact_number=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    occupation=models.TextField(max_length=250)
    added_on=models.DateTimeField(auto_now=True)
    update_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
ch=(
    ("Male","Male"),("Female","Female"),("other","other")
    )

class Doctor_Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=250,null=True)
    last_name=models.CharField(max_length=250,null=True)
    profile=models.ImageField(upload_to="media")
    contact_number=models.IntegerField()
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    occupation=models.TextField(max_length=250)
    added_on=models.DateTimeField(auto_now=True)
    update_on=models.DateTimeField(auto_now_add=True)
    patient=models.CharField(max_length=250,null=True)
    aap_time=models.CharField(max_length=250,null=True)
    contact=models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.user.username
ch=(
    ("Male","Male"),("Female","Female"),("other","other")
    )

class Addpatient(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=250)
    patient_img=models.ImageField(upload_to="media")
    patient_number=models.IntegerField()
    patient_address=models.CharField(max_length=250)
    patient_gender=models.CharField(max_length=250,choices=ch)

    def __str__(self):
        return self.seller.username

class Screening(models.Model):
    patient_name=models.CharField(max_length=250,null=True)
    symptoms=models.CharField(max_length=250)
    complains=models.CharField(max_length=250)
    bp=models.CharField(max_length=250)
    temperature=models.CharField(max_length=250)
    weight=models.CharField(max_length=250) 
    fever=models.CharField(max_length=250)
    pain_condition=models.CharField(max_length=250)
    physical_appearence=models.CharField(max_length=250)
    Deformation=models.CharField(max_length=250)
    appetite=models.CharField(max_length=250)
    sleep_conditions=models.CharField(max_length=250)

    def __str__(self):
        return self.symptoms


class Prescription(models.Model):
    p_name=models.CharField(max_length=200)
    medicine=models.CharField(max_length=100)
    quantity=models.IntegerField()
    days=models.CharField(max_length=50)
    time=models.CharField(max_length=100)

    def __str__(self):
        return self.medicine

class Appointment(models.Model):
    doctor = models.CharField(max_length=250)
    
    full_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250,null=True)
    phone_number=models.IntegerField()
   
    message=models.CharField(max_length=250)
    appointment_time=models.TimeField(max_length=12)
    appointment_date=models.DateField(max_length=12)

    def __str__(self):
        return self.doctor