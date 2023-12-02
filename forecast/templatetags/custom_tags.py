from django import template

register = template.Library()

@register.simple_tag
def change_flag(flag):
    
    return 'False'
