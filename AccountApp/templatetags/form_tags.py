# AccountApp/templatetags/form_tags.py
from django import template

register = template.Library()

@register.filter(name='add_form_group')
def add_form_group(field):
    return field.as_widget(attrs={"class": "form-control"})
