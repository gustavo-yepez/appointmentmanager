from django.shortcuts import render
from .forms import AppointmentTypeForm
from AppointmentApp.models import Appointment
from django.db.models import Count
from django.contrib.auth.decorators import login_required


@login_required
def ViewAppointmentType(request):
    form = AppointmentTypeForm()
    appointment_data = []

    if request.method == 'GET' and 'appointment_type' in request.GET:
        form = AppointmentTypeForm(request.GET)
        if form.is_valid():
            appointment_type = form.cleaned_data['appointment_type']
            appointment_data = Appointment.objects.filter(type=appointment_type).values('type').annotate(count=Count('id'))

    return render(request, 'ReportApp/ByTypes.html', {
        'form': form,
        'appointment_data': appointment_data,
    })

@login_required
def ViewAppointmentLocation(request):
    appointment_data = Appointment.objects.values('location').annotate(count=Count('id')).order_by('location')

    return render(request, 'ReportApp/ByLocation.html', {
        'appointment_data': appointment_data,
    })