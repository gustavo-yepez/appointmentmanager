from django.urls import path
from . import views

app_name = "ReportApp"

urlpatterns = [
    path('by_type/', views.ViewAppointmentType, name="ViewAppointmentType"),
    path('by_location/', views.ViewAppointmentLocation, name="ViewAppointmentLocation"),

]
