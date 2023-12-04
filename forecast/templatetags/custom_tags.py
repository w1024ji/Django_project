from django import template

register = template.Library()

@register.simple_tag
def change_flag_to_False(flag):
    
    return 'False'

@register.simple_tag
def change_flag_to_True(flag):

    return 'True'