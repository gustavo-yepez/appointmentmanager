from django import forms
from AppointmentApp.models import Appointment

class AppointmentTypeForm(forms.Form):
    type_choices = Appointment.objects.values_list('type', 'type').distinct()
    appointment_type = forms.ChoiceField(
        choices=type_choices,
        required=True,
        label="Select Appointment Type",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
