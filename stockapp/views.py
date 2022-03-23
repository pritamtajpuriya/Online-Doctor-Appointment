from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Appointment, Category,Admin_Register,Patient_Register,Doctor_Register, Prescription
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import Addpatient
from .forms import stockforms
from .models import Appointment

from .models import Contact,Screening
from django.core.mail import EmailMessage

def home(request):
    return render(request,'home.html')

def Admin_signup(request):
    msg=""
    if request.method=="POST":
        fname=request.POST['fname']
        passw=request.POST['passw']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        contact=request.POST['contact']
        age=request.POST['age']
        gender=request.POST['gender']  
        occu=request.POST['occupation']   
        utype=request.POST['utype']
        a=User.objects.filter(username=uname)
        if a:
            msg="User already exists"    
        else:
            us=User.objects.create_user(username=uname,email=email,password=passw)  
            us.first_name=fname
            us.last_name=lname
            us.username=uname
            us.email=email

            if "a" in utype:
                us.is_active=True
                us.is_staff=True
                us.is_superuser=True

          
   
                

            us.save()
            r=Admin_Register (user=us,contact_number=contact,age=age,gender=gender,occupation=occu)
            r.save()
          

            if "image" in request.FILES:
                img=request.FILES['image']
                r.profile=img
                r.save()
                msg="Sucessfully register"    
        return redirect('signin')    
    return render(request,'admin_signup.html')



def Patient_signup(request):
    msg=""
    if request.method=="POST":
        fname=request.POST['fname']
        passw=request.POST['passw']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        contact=request.POST['contact']
        age=request.POST['age']
        gender=request.POST['gender']  
        occu=request.POST['occupation']   
        utype=request.POST['utype']
        a=User.objects.filter(username=uname)
        if a:
            msg="User already exists"    
        else:
            us=User.objects.create_user(username=uname,email=email,password=passw)  
            us.first_name=fname
            us.last_name=lname
            us.username=uname
            us.email=email

          

            if "p" in utype:
                us.is_active=True 



   
                

            us.save()
            r=Patient_Register(user=us,contact_number=contact,age=age,gender=gender,occupation=occu)
            r.save()
          

            if "image" in request.FILES:
                img=request.FILES['image']
                r.profile=img
                r.save()
    msg="Sucessfully register"    
        #return redirect('signin')    
    return render(request,'patient_signup.html',{'msg':msg})

def Doctor_signup(request):
    msg=""
    if request.method=="POST":
        fname=request.POST['fname']
        print('my name '+fname)
        passw=request.POST['passw']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        contact=request.POST['contact']
        age=request.POST['age']
        gender=request.POST['gender']  
        occu=request.POST['occupation']   
        utype=request.POST['utype']
        a=User.objects.filter(username=uname)
        if a:
            msg="User already exists"    
        else:
            us=User.objects.create_user(username=uname,email=email,password=passw)  
            us.first_name=fname
            us.last_name=lname
            us.username=uname
            us.email=email

         
            if "d" in utype:
                us.is_staff=True

        


   
                

            us.save()
            r=Doctor_Register(user=us,first_name=fname,last_name=lname,contact_number=contact,age=age,gender=gender,occupation=occu)
            r.save()
          

            if "image" in request.FILES:
                img=request.FILES['image']
                r.profile=img
                r.save()
                msg="Sucessfully register"    
        return redirect('signin')    
    return render(request,'doctor_signup.html')



def signin(request):
    if request.method=="POST":
        uname=request.POST['uname']
        passw=request.POST['passw']
        print(uname,passw)

        a=authenticate(username=uname,password=passw)
        if a:
            login(request,a)
            if a.is_superuser:
                return redirect(dashboard)
            if a.is_staff:
                return redirect(dashboard)
            if a.is_active:
                return redirect(dashboard)
        else:
            msg="Invalid credintial"        
            return render(request,'signin.html',{'msg':msg})          
    return render(request,'signin.html')




def Admin_viewprofile(request):
    a=Admin_Register.objects.filter(user__id=request.user.id)
    if a:
        r=Admin_Register.objects.get(user__id=request.user.id)
        return render(request,'viewprofile.html',{'data':r})       
    else:
        msg="No data"
        return render(request,'viewprofile.html',{'msg':msg})          
    return render(request,'viewprofile.html')   

def Patient_viewprofile(request):
    a=Patient_Register.objects.filter(user__id=request.user.id)
    if a:
        r=Patient_Register.objects.get(user__id=request.user.id)
        return render(request,'viewprofile.html',{'data':r})       
    else:
        msg="No data"
        return render(request,'viewprofile.html',{'msg':msg})          
    return render(request,'viewprofile.html')   

def Doctor_viewprofile(request):
    a=Doctor_Register.objects.filter(user__id=request.user.id)
    if a:
        r=Doctor_Register.objects.get(user__id=request.user.id)
        return render(request,'viewprofile.html',{'data':r})       
    else:
        msg="No data"
        return render(request,'viewprofile.html',{'msg':msg})          
    return render(request,'viewprofile.html')   

def Admin_updateprofile(request):
    msg=""
    a=Admin_Register.objects.filter(user__id=request.user.id)
    if a:
        r=Admin_Register.objects.get(user__id=request.user.id)
        if request.method=='POST':
            fname=request.POST['fname']
            lname=request.POST['lname']
            uname=request.POST['uname']
            email=request.POST['email']
            contact=request.POST['contact']
            age=request.POST['age']
            gender=request.POST['gender']
            occupation=request.POST['occupation']
            usr=User.objects.get(id=request.user.id)
            usr.first_name=fname
            usr.last_name=lname
            usr.username=uname
            usr.email=email
            usr.save()
            r.user=usr
            r.contact_number=contact
            r.age=age
            r.gender=gender
            r.occupation=occupation
        
            if "image" in request.FILES:
                img=request.FILES['image']
                r.profile=img           
                msg="Profile Sucessfullyupdate"
            r.save()    
        return render(request,'updateprofile.html',{'data':r,'msg':msg}) 
    else:
        msg="No data"
        return render(request,'updateprofile.html',{'msg':msg})       
    return render(request,'updateprofile.html')    

def Patient_updateprofile(request):
    msg=""
    a=Patient_Register.objects.filter(user__id=request.user.id)
    if a:
        r=Patient_Register.objects.get(user__id=request.user.id)
        if request.method=='POST':
            fname=request.POST['fname']
            lname=request.POST['lname']
            uname=request.POST['uname']
            email=request.POST['email']
            contact=request.POST['contact']
            age=request.POST['age']
            gender=request.POST['gender']
            occupation=request.POST['occupation']
            usr=User.objects.get(id=request.user.id)
            usr.first_name=fname
            usr.last_name=lname
            usr.username=uname
            usr.email=email
            usr.save()
            r.user=usr
            r.contact_number=contact
            r.age=age
            r.gender=gender
            r.occupation=occupation
        
            if "image" in request.FILES:
                img=request.FILES['image']
                r.profile=img           
                msg=" Profile Sucessfully update"
            r.save()    
        return render(request,'updateprofile.html',{'data':r,'msg':msg}) 
    else:
        msg="No data"
        return render(request,'updateprofile.html',{'msg':msg})       
    return render(request,'updateprofile.html')

def Doctor_updateprofile(request):
    msg=""
    a=Doctor_Register.objects.filter(user__id=request.user.id)
    if a:
        r=Doctor_Register.objects.get(user__id=request.user.id)
        if request.method=='POST':
            fname=request.POST['fname']
            lname=request.POST['lname']
            uname=request.POST['uname']
            email=request.POST['email']
            contact=request.POST['contact']
            age=request.POST['age']
            gender=request.POST['gender']
            occupation=request.POST['occupation']
            usr=User.objects.get(id=request.user.id)
            usr.first_name=fname
            usr.last_name=lname
            usr.username=uname
            usr.email=email
            usr.save()
            r.user=usr
            r.contact_number=contact
            r.age=age
            r.gender=gender
            r.occupation=occupation
        
            if "image" in request.FILES:
                img=request.FILES['image']
                r.profile=img           
                msg="Profile Sucessfully update"
            r.save()    
        return render(request,'updateprofile.html',{'data':r,'msg':msg}) 
    else:
        msg="No data"
        return render(request,'updateprofile.html',{'msg':msg})       
    return render(request,'updateprofile.html')

def changepass(request):
    if request.method=="POST":
        current=request.POST['currentpass']
        change=request.POST['changepass']
        confirm=request.POST['confirmpass']
        usr=User.objects.get(id=request.user.id)
        b=usr.username
        v=usr.check_password(current)
        if v:
            if change==confirm:               
                usr.set_password(confirm)
                usr.save()
                us=User.objects.get(username=b)
                login(request,us)
                msg="Sucessfully changed password"
            else:
                msg="Password doesn't match"    
        else: 
            msg="Incorrect current password"   
        return render(request,'changepass.html',{'msg':msg})
    return render(request,'changepass.html')



def Admin_add_doctor(request):
    msg=""


    if request.method=="POST":
        fname=request.POST['fname']
        print('my name '+fname)
        passw=request.POST['passw']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        contact=request.POST['contact']
        age=request.POST['age']
        gender=request.POST['gender']  
        occu=request.POST['occupation']   
        utype=request.POST['utype']
        a=User.objects.filter(username=uname)
        if a:
            msg="User already exists"    
        else:

            us=User.objects.create_user(username=uname,email=email,password=passw)  
            us.first_name=fname
            us.last_name=lname
            us.username=uname
            us.email=email

         
            if "d" in utype:
                us.is_staff=True

            us.save()
            r=Doctor_Register(user=us,first_name=fname,last_name=lname,contact_number=contact,age=age,gender=gender,occupation=occu)
            r.save()
          

            if "image" in request.FILES:
                img=request.FILES['image']
                r.profile=img
                r.save()
                msg="Sucessfully register"    
        return redirect('aviewdoctor')    
    return render(request,'admin_add_doctor.html')


def Admin_add_patient(request):
    msg=""


    if request.method=="POST":
        fname=request.POST['fname']
        print('my name '+fname)
        passw=request.POST['passw']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        contact=request.POST['contact']
        age=request.POST['age']
        gender=request.POST['gender']  
        occu=request.POST['occupation']   
        utype=request.POST['utype']
        a=User.objects.filter(username=uname)
        if a:
            msg="User already exists"    
        else:

            us=User.objects.create_user(username=uname,email=email,password=passw)  
            us.first_name=fname
            us.last_name=lname
            us.username=uname
            us.email=email

         
            if "p" in utype:
                us.is_active=True 

            us.save()
            r=Patient_Register(user=us,first_name=fname,contact_number=contact,age=age,gender=gender,occupation=occu)
            r.save()
          

            if "image" in request.FILES:
                img=request.FILES['image']
                r.profile=img
                r.save()
                msg="Sucessfully register"    
        return redirect('aviewpatient')    
    return render(request,'admin_add_patient.html')


def addpatient(request):
    form=stockforms()
    if request.method=="POST":
        a=stockforms(request.POST,request.FILES)
        if a.is_valid():
            data=a.save(commit=False)
            u=User.objects.get(id=request.user.id)
            data.seller=u
            data.save()
            msg="Sucessfully Added"
        else:
            msg="Sorry not valid"    
        return render(request,'addpatient.html',{'form':form,'msg':msg})            
    return render(request,'addpatient.html',{'form':form})    

def contactus(request):
    contact_check=Contact.objects.all()
    if request.method=="POST":
        name = request.POST['name']
        contact_number = request.POST['number']
        subject = request.POST['subject']
        message = request.POST['message']
        contact=Contact(name=name,number=contact_number,subject=subject,message=message)
        contact.save()
        msg="Sucessfully Contact saved"
        print(request.POST)
        return render(request,'contactus.html',{'data':msg})

    return render(request,'contactus.html',{'Contactdata':contact_check})    

def dashboard(request):
    return render(request,'cust.html')

def service(request):
    return render(request,'service.html')    

def Admin_sendemail(request):
    data=""
    register=Admin_Register.objects.filter(user__id=request.user.id)
    if register:
        register=Admin_Register.objects.get(user__id=request.user.id)
        if request.method=="POST":
            rec=request.POST['to']
            subject=request.POST['subject']
            message=request.POST['message']
            try:
                em=EmailMessage(subject,message,to=[rec])
                em.send()
                data="Email sent"
                return render(request,'sendemail.html',{"data":data})
            except:
                data="Could not sent please check internet connection/Email address"
        return render(request,'sendemail.html',{"data":data})
           

    else:
        return render(request,'sendemail.html',{'data':"Sorry you don't have data"})    
    return render(request,'sendemail.html') 

def Patient_sendemail(request):
    data=""
    register=Patient_Register.objects.filter(user__id=request.user.id)
    if register:
        register=Patient_Register.objects.get(user__id=request.user.id)
        if request.method=="POST":
            rec=request.POST['to']
            subject=request.POST['subject']
            message=request.POST['message']
            try:
                em=EmailMessage(subject,message,to=[rec])
                em.send()
                data="Email sent"
                return render(request,'sendemail.html',{"data":data})
            except:
                data="Could not sent please check internet connection/Email address"
        return render(request,'sendemail.html',{"data":data})
           

    else:
        return render(request,'sendemail.html',{'data':"Sorry you don't have data"})    
    return render(request,'sendemail.html') 

def Doctor_sendemail(request):
    data=""
    register=Doctor_Register.objects.filter(user__id=request.user.id)
    if register:
        register=Doctor_Register.objects.get(user__id=request.user.id)
        if request.method=="POST":
            rec=request.POST['to']
            subject=request.POST['subject']
            message=request.POST['message']
            try:
                em=EmailMessage(subject,message,to=[rec])
                em.send()
                data="Email sent"
                return render(request,'sendemail.html',{"data":data})
            except:
                data="Could not sent please check internet connection/Email address"
        return render(request,'sendemail.html',{"data":data})
           

    else:
        return render(request,'sendemail.html',{'data':"Sorry you don't have data"})    
    return render(request,'sendemail.html') 



def logouts(request):
    logout(request)
    return render(request,'home.html')

def screening(request):
    if request.method=="POST":
        print(request.POST)
        patient_name=request.POST['patient_name']
        symptoms=request.POST['symptoms'] 
        complains=request.POST['complains'] 
        bp=request.POST['bp'] 
        temperature=request.POST['temperature']
        weight=request.POST['weight']
        fever=request.POST['fever']
        pain_condition=request.POST['pain_condition']
        physical_appearence=request.POST['physical_appearence']
        Deformation=request.POST['deformation']
        appetite=request.POST['appetite']
        sleep_conditions=request.POST['sleep_conditions']

        screening_object=Screening(patient_name=patient_name,symptoms=symptoms,complains=complains,bp=bp, temperature=temperature, weight=weight,fever=fever,pain_condition=pain_condition,physical_appearence=physical_appearence,Deformation=Deformation,appetite=appetite,sleep_conditions=sleep_conditions)
       
        screening_object.save()
        msz="Sucessfully Saved Screening"
        return render(request,'screening.html',{'msz':msz})    
    return render(request,'screening.html')  



def patient_view_screening(request):
    if request.method=="POST":
        patient=request.POST['sname']

        s_object=Screening.objects.filter(patient_name=patient)
        if s_object:
             return render(request,'patient_view_screening.html',{'obj':s_object})  
        else:
            msg="No patient found"
            return render(request,'patient_view_screening.html',{'msz':msg})       
    return render(request,'patient_view_screening.html')

 

     
def appointment(request):
    
    if request.method=="POST":
        
        doctor=request.POST['doctor']          
        full_name=request.POST['fname']  
        phone_number=request.POST['contact']
        email=request.POST['email']
        message=request.POST['message']
        appointment=request.POST['appointment']
        appointmentd=request.POST['appointmentd']
        
       
        
        appointment_object=Appointment(doctor=doctor,full_name=full_name, phone_number=phone_number,email=email,message=message,appointment_time=appointment,appointment_date=appointmentd)
        appointment_object.save()
        msz="Sucessfully Added Appointment"
        return render(request,'appointment.html',{'msz':msz})  
 
    return render(request,'appointment.html')       
   


def appointmentsent(request):
    if request.method=="POST":
        patient_name=request.POST['pname']

        appointment_object=Appointment.objects.filter(doctor=patient_name)
        if appointment_object:
             return render(request,'sentappointment.html',{'obj':appointment_object})  
        else:
            msg="No patient found"
            return render(request,'sentappointment.html',{'msz':msg})       
    return render(request,'sentappointment.html')


def adminviewappointment(request):
    user_check=Appointment.objects.all()
    d={'user_check':user_check}
    return render(request,'adminviewappointment.html',d) 


def patientviewappointment(request):
    if request.method=="POST":

        patient_name=request.POST['fname']
        anil=Appointment.objects.filter(full_name=patient_name)
        if anil:
             return render(request,'patientviewappointment.html',{'obj':anil})  
        else:
            msg="No patient found"
            return render(request,'patientviewappointment.html',{'msz':msg})
    return render(request,'patientviewappointment.html')
   

    

def search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        anil=Doctor_Register.objects.filter(occupation__contains=searched)
        return render(request,'viewdoctor.html',{'searched':searched,'anil':anil})
    else:
        return render(request,'viewdoctor.html')
        
def aboutus(request):
    return render(request,'aboutus.html')

def delete(request,id):
    Appointment.objects.get(id=id).delete()
    return redirect('/appointmentsent/') 

def Admin_delete_appointment(request,id):
    Appointment.objects.get(id=id).delete()
    return redirect('/adminviewappointment/')

def patient_delete_appointment(request,id):
    Appointment.objects.get(id=id).delete()
    return redirect('/patientviewappointment/')    


def delete_doctor(request,id):
    Doctor_Register.objects.get(id=id).delete()
    return redirect('/aviewdoctor/') 

def delete_patient(request,id):
    Patient_Register.objects.get(id=id).delete()
    return redirect('/aviewpatient/') 

    
def viewdoctor(request):
    user_check=Doctor_Register.objects.all()

    return render(request,'viewdoctor.html',{'all':user_check})      
    # return render(request,'viewdoctor.html')      

def adminviewdoctor(request):
    user_check=Doctor_Register.objects.all()

    return render(request,'adminviewDoctors.html',{'all':user_check})     


def adminviewpatient(request):
    user_check=Patient_Register.objects.all()

    return render(request,'adminviewPatients.html',{'all':user_check}) 



def prescription(request):

    if request.method=="POST":
        print(request.POST)
        patient=request.POST['patientname']
        medicine=request.POST['medicine'] 
        quantity=request.POST['quantity'] 
        days=request.POST['days']
        time=request.POST['time'] 
        prescription_object=Prescription(p_name=patient,medicine=medicine, quantity=quantity, days=days, time=time)
     
       
        prescription_object.save()
        msz="Sucessfully send prescripton to patient"
        return render(request,'addprescription.html',{'msz':msz})    
    return render(request,'addprescription.html')  

def patient_view_prescription(request):
    if request.method=="POST":
        patients=request.POST['prname']
        prescription_object=Prescription.objects.filter(p_name=patients)
        if prescription_object:
             return render(request,'patientviewprescription.html',{'abc':prescription_object})  
        else:
            msg="No patient found"
            return render(request,'patientviewprescription.html',{'msz':msg})       
    return render(request,'patientviewprescription.html')    


