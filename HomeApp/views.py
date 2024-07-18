from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm
from AccountApp.models import Customer
from django.contrib.auth.decorators import login_required


def HomeView(request):
    return render(request, "HomeApp/HomeView.html")

@login_required
def CustomerView(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HomeApp:ViewHome')
    else:
        form = CustomerForm()
    return render(request, "HomeApp/CustomerView.html", {'form':form})

@login_required
def CustomerListView(request):
    customer = Customer.objects.all()
    return render(request, "HomeApp/CustomerList.html", {'customers':customer})

@login_required
def CustomerUpdateView(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('HomeApp:ViewCustomerList')
    else:
        form = CustomerForm(instance=customer)
    return render(request, "HomeApp/CustomerView.html", {'form': form, 'customer': customer})


@login_required
def CustomerDeleteView(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    customer.delete()
    return redirect('HomeApp:ViewCustomerList')


@login_required
def AppointmentView(request):
    return render(request, "HomeApp/AppointmentView.html")

@login_required
def ReportView(request):
    return render(request, "HomeApp/ReportView.html")
