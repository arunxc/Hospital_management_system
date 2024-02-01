"""
URL configuration for hosp_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hosp_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.start, name='start'),
    path('home/',views.home, name='home'),
    path('about/', views.about, name='about'),
    path("contact/",views.contact, name='contact'),
    path("login_admin/",views.login_admin, name='login_admin'),
    path("logout_admin/",views.logout_admin, name='logout_admin'),
    path("index/",views.index,name = "index"),
    path("view_doctor/",views.view_doctor,name = "view_doctor"),
    path("view_patient/",views.view_patient,name = "view_patient"),
    path("view_appointment/",views.view_appointment,name = "view_appointment"),
    path("delete_doctor/<id>",views.delete_doctor,name = "delete_doctor"),
    path("delete_patient/<id>",views.delete_patient,name = "delete_patient"),
    path("delete_appointment/<id>",views.delete_appointment,name = "delete_appointment"),
    path("add_doctor/",views.add_doctor,name = "add_doctor"),
    path("add_patient/",views.add_patient,name = "add_patient"),
    path("add_appointment/",views.add_appointment,name = "add_appointment"),
    path("doctor_login/",views.doctor_login,name = "doctor_login"),
    path("doctor_register",views.doctor_register,name = "doctor_register"),
]
