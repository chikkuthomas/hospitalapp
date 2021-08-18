from django import forms
from django.forms import ModelForm
from .models import Doctors

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


