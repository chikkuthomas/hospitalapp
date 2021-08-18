from django.db import models
from django.utils import timezone
# Create your models here.


class Doctors(models.Model):
    doctor_name=models.CharField(max_length=120)
    speciality=models.CharField(max_length=250)
    image = models.ImageField(upload_to="images")
    specialist=models.CharField(max_length=120)
    about=models.CharField(max_length=500)
    date=models.DateField(default=timezone.now)
    start_time=models.TimeField(max_length=250)
    end_time=models.TimeField(max_length=250)
    availability=models.CharField(max_length=120)




