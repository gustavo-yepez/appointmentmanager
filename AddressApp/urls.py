from django.urls import path
from . import views

app_name = "AddressApp"

urlpatterns = [
    path('add_country/', views.AddCountryView, name="ViewAddCountry"),
    path('add_city/', views.AddCityView, name="ViewAddCity"),
]
