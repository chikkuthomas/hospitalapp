from django.shortcuts import render,redirect
from .models import Doctors
from .forms import DoctorAddForm,DoctorUpdateForm
from django.views.generic import TemplateView,ListView,DetailView,CreateView,DeleteView
from patient.models import Patients
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
# def doctoradd(request):
#     context={}
#     form=DoctorAddForm()
#     context["form"]=form
#     if request.method=="POST":
#         form=DoctorAddForm(request.POST,request.FILES) #to get image file
#         if form.is_valid():
#             form.save()
#         else:
#             context["form"] = form
#             return render(request, "doctoraddform.html", context)
#
#     return render(request,"doctoraddform.html",context)



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

class PatientsListView(ListView):
    template_name = "patient_details.html"
    model=Patients
    context_object_name = "patients"






