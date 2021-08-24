from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from patient import forms
from doctor.models import Doctors
from .models import Patients
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView


# registration
class UserRegistrationView(TemplateView):
    form_class=forms.RegistrationForm
    template_name = "registration.html"    #to render this html page
    model=User
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class SigninView(TemplateView):
    template_name = "signin.html"
    form_class=forms.LoginForm
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("patienthome")
            else:
                self.context["form"] = form
                return render(request, self.template_name, self.context)

class SignOutView(TemplateView):
    def get(self,request, *args, **kwargs):
        logout(request)
        return redirect("signin")


class PatientHome(TemplateView):
    template_name="patient_home.html"

class DoctorsView(ListView):
    template_name = "doctorsdetail.html"
    model = Doctors
    context_object_name = "doctors"

class PatientFillUpForm(CreateView):
    model = Patients
    template_name = "patient_fillupform.html" #createview will render the form in the html
    form_class =forms.PatientForm  #form from forms.py for the html page
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST) #getting values from the form fields when sbmitted
        if form.is_valid():
            # initially form is not saved, bcs we need to get values of other fields in the model Patient
            patient = form.save(commit=False)
            doctor_id = kwargs["d_id"]
            doctor =Doctors.objects.get(id=doctor_id)
            patient.doctor=doctor
            patient.user = request.user  # signed in user to the user field of model
            patient.status = "booked_slot"
            patient.save()
            return redirect("patienthome")

class AppoinmentStatusView(ListView):
    template_name = "appoinment_status.html"
    model = Patients
    context_object_name = "patients"
    #here we need only the orders of specific user ,the user who logged in
    def get_queryset(self):
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset

class CancelAppoinmentView(DeleteView):
    model=Patients
    def get(self, request, *args, **kwargs):
        id=kwargs['id']
        patient=Patients.objects.get(id=id)
        patient.delete()
        return redirect("appoinmentsview")
