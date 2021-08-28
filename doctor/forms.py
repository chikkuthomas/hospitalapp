from django import forms
from django.forms import ModelForm
from .models import Doctors
from patient.models import Patients

class DoctorAddForm(ModelForm):
    class Meta:
        model=Doctors
        fields="__all__"
        widgets = {
            "doctor_name": forms.TextInput(attrs={"class": "form-control"}),
            "speciality": forms.TextInput(attrs={"class": "form-control"}),
            "specialist": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "about": forms.Textarea(attrs={"class": "form-control"}),
            "date":forms.SelectDateWidget(attrs={"class": "form-control"}),
            "availability": forms.TextInput(attrs={"class": "form-control"}),
            "start_time": forms.NumberInput(attrs={"class": "form-control","type":"time"}),
            "end_time": forms.NumberInput(attrs={"class": "form-control","type":"time"})
        }

class DoctorUpdateForm(ModelForm):
    class Meta:
        model=Doctors
        fields="__all__"
        widgets = {
            "doctor_name": forms.TextInput(attrs={"class": "form-control"}),
            "speciality": forms.TextInput(attrs={"class": "form-control"}),
            "specialist": forms.TextInput(attrs={"class": "form-control"}),
            # "image": forms.FileInput(attrs={"class": "form-control"}),
            "about": forms.Textarea(attrs={"class": "form-control"}),
            "date":forms.SelectDateWidget(attrs={"class": "form-control"}),
            "availability": forms.TextInput(attrs={"class": "form-control"}),
            "start_time": forms.NumberInput(attrs={"class": "form-control","type":"time"}),
            "end_time": forms.NumberInput(attrs={"class": "form-control","type":"time"})
        }

class PatientUpdateForm(ModelForm):
    class Meta:
        model=Patients
        fields=[
            "patient_name","doctor","age","time_slot","status"
        ]
        widgets={
            "status":forms.Select(attrs={"class": "form-select"}),
            "time_slot": forms.NumberInput(attrs={"class": "form-control","type":"time"}),
            "patient_name":forms.TextInput(attrs={"class":"form-control","readonly":True}),
            "doctor": forms.TextInput(attrs={"class": "form-control", "readonly": True}),
            "age": forms.NumberInput(attrs={"class": "form-control", "readonly": True})
        }

