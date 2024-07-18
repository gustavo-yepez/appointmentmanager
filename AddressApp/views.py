from django.shortcuts import render, redirect
from .forms import CityForm, CountryForm
from django.contrib.auth.decorators import login_required

@login_required
def AddCityView(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HomeApp:ViewHome')
    else:
        form = CityForm()
    return render(request, 'AddressApp/AddCityView.html', {'form':form})
@login_required
def AddCountryView(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HomeApp:ViewHome')
    else:
        form = CountryForm()
    return render(request, 'AddressApp/AddCountryView.html', {'form':form})
