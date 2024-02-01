from django.db import models

# Create your models here.
class doctorModel(models.Model):
    name = models.CharField(max_length = 50,null = True)
    mobile = models.TextField()
    special = models.CharField(max_length = 50,null = True)

    def __str__(self):
        return self.name

class patientModel(models.Model):
    name = models.CharField(max_length = 50,null = True)
    gender = models.CharField(max_length = 10, null = True)
    mobile = models.TextField(null = True)
    address = models.TextField()

    def __str__(self):
        return self.name

class appointmentModel(models.Model):
    doctor = models.ForeignKey(doctorModel,on_delete = models.CASCADE)
    patient = models.ForeignKey(patientModel,on_delete = models.CASCADE)
    data = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.doctorModel.name+"__"+self.patientModel.name

class doctorRegisterModel(models.Model):
    name = models.TextField(max_length = 255)
    password = models.TextField()