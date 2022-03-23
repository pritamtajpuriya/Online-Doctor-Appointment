from django.contrib import admin
from .models import Category,Admin_Register,Patient_Register,Doctor_Register,Addpatient,Contact, Prescription,Screening,Appointment
# Register your models here.

admin.site.register(Category)
admin.site.register(Admin_Register)
admin.site.register(Patient_Register)
admin.site.register(Doctor_Register)
admin.site.register(Addpatient)
admin.site.register(Contact)
admin.site.register(Screening)
admin.site.register(Appointment)
admin.site.register(Prescription)