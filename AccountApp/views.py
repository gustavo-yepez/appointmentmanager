from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm

@login_required
def RegisterUserView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('HomeApp:ViewHome')
    else:
        form = UserRegistrationForm()
    return render(request, 'AccountApp/SignupView.html', {'form': form})

def LoginView(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('HomeApp:ViewHome')
    else:
        form = UserLoginForm()
    return render(request, 'AccountApp/LoginView.html', {'form': form})

@login_required
def LogoutView(request):
    logout(request)
    return redirect('AccountApp:ViewLogin')
