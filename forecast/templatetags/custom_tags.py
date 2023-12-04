from django import template

register = template.Library()

# Django template 문법에는 break가 없어서 고민하다가 flag를 만듦

@register.simple_tag
def change_flag_to_False(flag):
    
    return 'False'

@register.simple_tag
def change_flag_to_True(flag):

    return 'True'