from django.db import models
from doctor.models import Doctors

# Create your models here.

class Patients(models.Model):
    patient_name=models.CharField(max_length=120)
    doctor=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    age=models.PositiveIntegerField(blank=False)
    gender=models.CharField(max_length=20)
    options = (
        ("booked_slot", "booked_slot"),  # 1st value , 2nd display
        ("cancelled_appoinment", "cancelled_appoinment"),
        ("no_booking", "no_booking"),
        ("appointed","appointed")

    )
    time_slot=models.TimeField(max_length=250,null=True)
    status = models.CharField(max_length=40, default="no_booking", choices=options)
    user = models.CharField(max_length=40)
