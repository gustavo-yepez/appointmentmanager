from django import forms
from .models import Appointment
from AccountApp.models import UserProfile, Customer, User

class AppointmentForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True)
    booked_by = forms.ModelChoiceField(queryset=User.objects.all(), required=True)
    title = forms.CharField(max_length=255, required=True)
    description = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    location = forms.CharField(max_length=255, required=True)
    contact = forms.CharField(max_length=255, required=True)
    type = forms.CharField(max_length=255, required=True)
    url = forms.URLField(required=False)
    start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Appointment
        fields = '__all__'
