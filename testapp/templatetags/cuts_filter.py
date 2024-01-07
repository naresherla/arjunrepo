from django import template
register= template.Library()
def first_upper(value):
    result = value[0:1].upper()
    return result
register.filter('ffu',first_upper)