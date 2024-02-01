from django.contrib import admin
from hosp_app import models

# Register your models here.
admin.site.register(models.doctorModel)
admin.site.register(models.patientModel)
admin.site.register(models.appointmentModel)
