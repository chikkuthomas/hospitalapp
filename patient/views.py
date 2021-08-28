from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from patient import forms
from doctor.models import Doctors
from .models import Patients
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView
from django.utils.decorators import method_decorator
from .decorators import sign_in_requierd


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
                if user.is_superuser:
                    return redirect("home")
                return redirect("patienthome")
            else:
                self.context["form"] = form
                return render(request, self.template_name, self.context)

@method_decorator(sign_in_requierd,name="dispatch")
class SignOutView(TemplateView):
    def get(self,request, *args, **kwargs):
        logout(request)
        return redirect("signin")

@method_decorator(sign_in_requierd,name="dispatch")
class PatientHome(TemplateView):
    template_name="patient_home.html"

@method_decorator(sign_in_requierd,name="dispatch")
class DoctorsView(ListView):
    template_name = "doctorsdetail.html"
    model = Doctors
    context_object_name = "doctors"

@method_decorator(sign_in_requierd,name="dispatch")
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

@method_decorator(sign_in_requierd,name="dispatch")
class AppoinmentStatusView(ListView):
    template_name = "appoinment_status.html"
    model = Patients
    context_object_name = "patients"
    #here we need only the orders of specific user ,the user who logged in
    def get_queryset(self):
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset

@method_decorator(sign_in_requierd,name="dispatch")
class CancelAppoinmentView(DeleteView):
    model=Patients
    def get(self, request, *args, **kwargs):
        id=kwargs['id']
        patient=Patients.objects.get(id=id)
        patient.delete()
        return redirect("appoinmentsview")
