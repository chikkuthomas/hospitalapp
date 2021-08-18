from django.urls import path
from doctor import views
urlpatterns=[
    path("home",views.Home.as_view(),name="home"),
    path("doctoradd",views.DoctorCreateView.as_view(),name="doctoradd"),
    path("doctorlist",views.DoctorsListView.as_view(),name="doctorlist"),
    path("doctorupdate/<int:id>",views.doctor_update,name="doctorupdate"),
    path("doctordetail/<int:id>",views.DoctorDetailView.as_view(),name="doctordetail"),
    path("doctor_remove/<int:id>",views.RemoveDoctor.as_view(),name="doctorremove"),
    path("patient_details", views.PatientsListView.as_view(), name="patient_list"),

]