from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def space_to_underscore(value):
    return value.replace(' ', '_')