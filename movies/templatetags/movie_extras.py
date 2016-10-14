from django import template

register = template.Library()

@register.filter
def join_name_elements_by(value, arg):
    l = [x['name'] for x in value]
    return arg.join(l)