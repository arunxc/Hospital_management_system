from hosp_app import models

doctor = models.doctorModel.objects.all()
arr = []

arr2 = arr.append(doctor)
print("hiiii")
print(len(arr2))

