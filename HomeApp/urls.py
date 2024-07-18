from django.urls import path
from . import views

app_name = "HomeApp"

urlpatterns = [
    path('', views.HomeView, name="ViewHome"),
    path('Customer/', views.CustomerView, name="ViewCustomer"),
    path('Appointment/', views.AppointmentView, name="ViewAppointment"),
    path('Report/', views.ReportView, name="ViewReport"),

    path('Customer_List/', views.CustomerListView, name="ViewCustomerList"),
    path('Customer/update/<int:pk>/', views.CustomerUpdateView, name="ViewCustomerUpdate"),
    path('Customer/delete/<int:pk>/', views.CustomerDeleteView, name="ViewCustomerDelete"),
]
