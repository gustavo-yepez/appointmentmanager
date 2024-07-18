from django.urls import path
from . import views

app_name = "AppointmentApp"

urlpatterns = [
    path('Create/', views.AppointmentView, name="ViewAppointment"),
    path('Appointments_List/', views.AppointmentListView, name='ViewAppointmentList'),
    path('Update_Appointments/<int:pk>/', views.AppointmentUpdateView, name='ViewAppointmentUpdate'),
    path('Delete_Appointments/<int:pk>/', views.AppointmentDeleteView, name='ViewAppointmentDelete'),
]
