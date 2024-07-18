from django import forms
from AccountApp.models import Customer
from AddressApp.models import Address, City, Country

class CustomerForm(forms.ModelForm):
    address_line1 = forms.CharField(max_length=255, required=True)
    address_line2 = forms.CharField(max_length=255, required=False)
    postal_code = forms.CharField(max_length=20, required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=True)
    is_active = forms.BooleanField(required=False)

    class Meta:
        model = Customer
        fields = ['name', 'is_active']

    def __init__(self, *args, **kwargs):
        customer = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if customer and customer.address:
            self.fields['address_line1'].initial = customer.address.line1
            self.fields['address_line2'].initial = customer.address.line2
            self.fields['postal_code'].initial = customer.address.postal_code
            self.fields['phone_number'].initial = customer.address.phone_number
            self.fields['city'].initial = customer.address.city
            self.fields['country'].initial = customer.address.city.country

    def save(self, commit=True):
        customer = super().save(commit=False)
        address, created = Address.objects.get_or_create(
            line1=self.cleaned_data['address_line1'],
            line2=self.cleaned_data['address_line2'],
            city=self.cleaned_data['city'],
            postal_code=self.cleaned_data['postal_code'],
            phone_number=self.cleaned_data['phone_number']
        )
        if not created:
            address.line1 = self.cleaned_data['address_line1']
            address.line2 = self.cleaned_data['address_line2']
            address.city = self.cleaned_data['city']
            address.postal_code = self.cleaned_data['postal_code']
            address.phone_number = self.cleaned_data['phone_number']
            address.save()
        customer.address = address
        if commit:
            customer.save()
        return customer
