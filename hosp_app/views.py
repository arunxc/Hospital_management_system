from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from hosp_app.models import doctorModel,patientModel,appointmentModel,doctorRegisterModel

# Create your views here.
def about(request):
    return render(request,"about.html")

def start(request):
    return render(request,"nav_login.html")

def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")

def index(request):
    
    if not request.user.is_staff:
        return redirect("/admin_login/")
    doctors = doctorModel.objects.count()
    patients = patientModel.objects.count()
    appointments  = appointmentModel.objects.count()
    
    d = doctors
    p = patients
    a = appointments
    
    return render(request,'index.html', {'d' : d, 'p' : p, 'a' : a,})

def login_admin(request):
    error = ""
    if request.method=="POST":
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username = name,password = password)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

        
    d = {
        'error' : error
    }
            
    return render(request,"login.html",d)

def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    
    logout(request)
    return redirect('start')


def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = doctorModel.objects.all()
    d = {
        'doc': doc
    }
    return render(request,"view_doctor.html",d)

def delete_doctor(request,id):
    if not request.user.is_staff:
        return redirect('login_admin')
    doctor = doctorModel.objects.get(id=id)
    doctor.delete()
    return redirect("view_doctor")

def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect("login_admin")
    if request.method=="POST":
        name = request.POST['name']
        mobile = request.POST['mobile']
        special = request.POST['special']

        try:
            doctorModel.objects.create(name= name,mobile = mobile,special = special)
            error="no"
        except:
            error = "yes"
    d = {
        'error' : error
    }
    
    return render(request,"add_doctor.html",d)

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    doc = patientModel.objects.all()
    d = {
        'doc': doc
    }
    return render(request,"view_patient.html",d)

def delete_patient(request,id):
    if not request.user.is_staff:
        return redirect('login_admin')
    patient = patientModel.objects.get(id=id)
    patient.delete()
    return redirect("view_patient")

def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect("login_admin")
    if request.method=="POST":
        name = request.POST['name']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        address = request.POST['address']

        try:
            patientModel.objects.create(name= name, gender = gender, mobile = mobile, address = address,)
            error="no"
        except:
            error = "yes"
    d = {
        'error' : error
    }
    
    return render(request,"add_patient.html",d)

def add_appointment(request):
    error = ""
    dr = ""
    pa = ""
    if not request.user.is_staff:
        return redirect("login_admin")
    pa1 = patientModel.objects.all()
    dr1 = doctorModel.objects.all()
    if request.method=="POST":
        doctor = request.POST['doctor']
        patient = request.POST['patient']
        data = request.POST['date']
        time = request.POST['time']
        dr = doctorModel.objects.filter(name = doctor).first()
        pa = patientModel.objects.filter(name = patient).first()

        try:
            appointmentModel.objects.create(doctor = dr, patient = pa, data = data, time = time,)
            error="no"
            
        except:
            error = "yes"
        print(dr)
    d = {
        'dr' :dr1,
        'pa' : pa1,
        'error' : error,
        
    }
    print(error)
    
    return render(request,"add_appointment.html",d)

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    doc = appointmentModel.objects.all()
    d = {
        'doc': doc
    }
    return render(request,"view_appointment.html",d)

def delete_appointment(request,id):
    if not request.user.is_staff:
        return redirect('login_admin')
    patient = appointmentModel.objects.get(id=id)
    patient.delete()
    return redirect("view_appointment")

def doctor_login(request):
    error = ""
    if request.method=="POST":

        data = doctorRegisterModel.objects.get(name = request.POST['name'])

        name = request.POST['name']
        password = request.POST['password']

        if data.name==name and data.password==password:
            print("success")
            error="no"

        else:
            print("error")
            error = "yes"
    d = {
        'error' : error
    }
            
    return render(request,"doctor_login.html",d)

def doctor_register(request):
    error = ''
    if request.method=="POST":
        name = request.POST['name']
        password = request.POST['password']
        confirmpass = request.POST['confirmpassword']

        if password!=confirmpass:
            error = "yes"
        elif password==confirmpass:
            data = doctorRegisterModel.objects.create(
                name = name,
                password = password,
            )
            data.save()
            error = "no"
            print("helloo")

    print(error)
    print("hiiii")
    context = {
        'error' : error
    }
    return render(request,"doctor_register.html",context)