from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("HomeApp.urls")),
    path('Account/', include("AccountApp.urls")),
    path('Address/', include("AddressApp.urls")),
    path('Appointment/', include("AppointmentApp.urls")),
    path('Report/', include("ReportApp.urls")),
]
