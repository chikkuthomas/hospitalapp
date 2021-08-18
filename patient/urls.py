from django.urls import path
from patient import views
urlpatterns=[
path("accounts/signin",views.SigninView.as_view(),name="signin"),
    path("accounts/signup",views.UserRegistrationView.as_view(),name="signup"),
    path("accounts/signout",views.SignOutView.as_view(),name="signout"),
    path("home",views.PatientHome.as_view(),name="patienthome"),
    path("appoinments",views.DoctorsView.as_view(),name="doctorsview"),
    path("patientform/<int:d_id>",views.PatientFillUpForm.as_view(),name="fillupform"),
    path("viewappoinments", views.AppoinmentStatusView.as_view(), name="appoinmentsview"),
    path("cancelappoinment/<int:id>", views.CancelAppoinmentView.as_view(), name="cancelappoinment"),

]