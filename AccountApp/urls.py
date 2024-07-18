from django.urls import path
from . import views

app_name = "AccountApp"

urlpatterns = [
    path('register/', views.RegisterUserView, name="ViewRegisterUser"),
    path('login/', views.LoginView, name="ViewLogin"),
    path('logout/', views.LogoutView, name="ViewLogout"),
]
