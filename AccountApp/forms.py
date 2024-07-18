from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from AddressApp.models import Address, City
from AccountApp.models import UserProfile

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class UserRegistrationForm(BootstrapFormMixin, UserCreationForm):
    email = forms.EmailField(required=True)
    address_line1 = forms.CharField(max_length=255, required=True)
    address_line2 = forms.CharField(max_length=255, required=False)
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
    postal_code = forms.CharField(max_length=20, required=True)
    phone_number = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            address = Address.objects.create(
                line1=self.cleaned_data['address_line1'],
                line2=self.cleaned_data['address_line2'],
                city=self.cleaned_data['city'],
                postal_code=self.cleaned_data['postal_code'],
                phone_number=self.cleaned_data['phone_number']
            )
            UserProfile.objects.create(user=user, address=address)
        return user

class UserLoginForm(BootstrapFormMixin, AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
