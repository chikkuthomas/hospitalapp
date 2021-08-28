from django.shortcuts import render,redirect
from .models import Doctors
from .forms import DoctorAddForm,DoctorUpdateForm,PatientUpdateForm
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from patient.models import Patients
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

class Home(TemplateView):
    template_name="home.html"

class DoctorCreateView(CreateView):
    model = Doctors
    template_name = "doctoraddform.html" #createview will render the form in the html
    form_class = DoctorAddForm #form from forms.py for the html page
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST,request.FILES) #getting values from the form fields when sbmitted
        if form.is_valid():
            form.save()
            return redirect("home")

class DoctorsListView(ListView):
    template_name = "doctorslist.html"
    model=Doctors
    context_object_name = "doctors"

def doctor_update(request,id):
    doctor = Doctors.objects.get(id=id)
    form = DoctorUpdateForm(instance=doctor)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = DoctorUpdateForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("doctorlist")
        else:
            context["form"] = form
            return render(request, "doctor_edit.html", context)
    return render(request, "doctor_edit.html", context)

class DoctorDetailView(DetailView):
    template_name = "doctordetail.html"
    model = Doctors
    context_object_name = "doctor"
    pk_url_kwarg = 'id'

class RemoveDoctor(DeleteView):
    model = Doctors
    def get(self, request, *args, **kwargs):
        id=kwargs["id"]
        doctor=Doctors.objects.get(id=id)
        doctor.delete()
        return redirect("doctorlist")

class PatientsListView(TemplateView):
    template_name = "patient_details.html"
    context={}
    def get(self, request, *args, **kwargs):
        booking_count=Patients.objects.filter(status="booked_slot").count()
        self.context["booking_count"]=booking_count
        patients=Patients.objects.filter(status="booked_slot")
        self.context["patients"] = patients
        appointed_count=Patients.objects.filter(status="appointed").count()
        self.context["appointed_count"] = appointed_count
        appointed=Patients.objects.filter(status="appointed")
        self.context["appointed"] = appointed
        return render(request,self.template_name,self.context)

class PatientUpdate(UpdateView):
    model = Patients
    template_name = "patientupdate.html"
    pk_url_kwarg = 'id'
    form_class = PatientUpdateForm
    success_url = reverse_lazy("home")





