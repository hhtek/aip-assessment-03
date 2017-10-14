"""
This custom form template tag filter are used to control the 'PasswordInput' field
not to use CSS class 'is-valid' when the form is bound back to user when user
enter username and password combination incorrectly.

This template tag filter is used with 'snippets/form.html' using with
widget_tweaks library.

Reference: https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html#creating-custom-template-tags
"""
from django import template

register = template.Library()

@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__

@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)
