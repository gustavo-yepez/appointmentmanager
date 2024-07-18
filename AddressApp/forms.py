from django import forms
from AddressApp.models import City, Country

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country']

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
