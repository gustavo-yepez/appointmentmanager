from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm
from .models import Appointment
from django.utils import timezone
from .models import Appointment
from datetime import timedelta
from django.contrib.auth.decorators import login_required

@login_required
def AppointmentView(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppointmentApp:ViewAppointmentList')  # Replace with your actual URL name
    else:
        form = AppointmentForm()
    return render(request, "AppointmentApp/CreateAppointmentView.html", {'form': form})

@login_required
def AppointmentUpdateView(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('AppointmentApp:ViewAppointmentList')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, "AppointmentApp/CreateAppointmentView.html", {'form': form, 'customer': appointment})
@login_required
def AppointmentDeleteView(request, pk):
    get_appointment = Appointment.objects.get(id=pk)
    if get_appointment:
        get_appointment.delete()
        return redirect("AppointmentApp:ViewAppointmentList")
@login_required
def AppointmentListView(request):
    appointments = Appointment.objects.all()

    filter_option = request.GET.get('filter', 'all')
    selected_date = request.GET.get('date', None)

    if filter_option == 'date' and selected_date:
        appointments = appointments.filter(start_time__date=selected_date)
    elif filter_option == 'current_month':
        now = timezone.now()
        appointments = appointments.filter(start_time__year=now.year, start_time__month=now.month)
    elif filter_option == 'current_week':
        now = timezone.now()
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        appointments = appointments.filter(start_time__date__range=(start_of_week, end_of_week))

    return render(request, 'AppointmentApp/AppointmentListView.html', {'appointments': appointments})