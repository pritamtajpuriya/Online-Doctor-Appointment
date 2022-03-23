from django.urls import path
from .import views


urlpatterns = [
    path('', views.home,name="home"),

    path('asignup/', views.Admin_signup,name="asignup"),
    path('psignup/', views.Patient_signup,name="psignup"),
    path('dsignup/', views.Doctor_signup,name="dsignup"),
    path('signin/', views.signin,name="signin"),
    path('aviewprofile/', views.Admin_viewprofile,name="aviewprofile"),
    path('pviewprofile/', views.Patient_viewprofile,name="pviewprofile"),
    path('dviewprofile/', views.Doctor_viewprofile,name="dviewprofile"),
    path('aupdateprofile/', views.Admin_updateprofile,name="aupdateprofile"),
    path('pupdateprofile/', views.Patient_updateprofile,name="pupdateprofile"),
    path('dupdateprofile/', views.Doctor_updateprofile,name="dupdateprofile"),
    path('changepass/', views.changepass,name="changepass"),
    path('addpatient/', views.addpatient,name="addpatient"),  
    path('contactus/', views.contactus,name="contactus"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('service/', views.service,name="service"),
    path('asendemail/', views.Admin_sendemail,name="asendemail"),
    path('psendemail/', views.Patient_sendemail,name="psendemail"),
    path('dsendemail/', views.Doctor_sendemail,name="dsendemail"),
    path('logouts/', views.logouts,name="logouts"),
    path('screening/', views.screening,name="screening"),
    path('appointment/', views.appointment,name="appointment"),
    path('aboutus/', views.aboutus,name="aboutus"),
    path('appointmentsent/', views.appointmentsent,name="appointmentsent"),
    path('delete/<int:id>',views.delete, name="deletepost"),
    path('doc_delete/<int:id>',views.delete_doctor, name="deletedoctor"),
    path('pat_delete/<int:id>',views.delete_patient, name="deletepatient"),
    path('admin_delete_appointment/<int:id>',views.Admin_delete_appointment, name="Admin_delete_appointment"),
    path('patient_delete_appointment/<int:id>',views.patient_delete_appointment, name="patient_delete_appointment"),
    path('viewdoctor/', views.viewdoctor,name="viewdoctor"),

    path('search/', views.search,name="search"),    

    path('adminadddoctor/',views.Admin_add_doctor,name="adminadddoctor"),
    path('adminaddpatient/',views.Admin_add_patient,name="adminaddpatient"),
    path('adminviewappointment/',views.adminviewappointment,name="adminviewappointment"),
    path('patientviewappointment/',views.patientviewappointment,name="patientviewappointment"),
    path('aviewdoctor/', views.adminviewdoctor,name="aviewdoctor"),
    path('aviewpatient/', views.adminviewpatient,name="aviewpatient"),
    path('patient_view_screening/',views.patient_view_screening,name="patient_view_screening"),
    path('prescription/',views.prescription,name="prescription"),
    path('viewprescription/',views.patient_view_prescription,name="viewprescription")


]
