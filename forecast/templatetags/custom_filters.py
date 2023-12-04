from django import template
from django.utils.html import format_html
from django.conf import settings

register = template.Library()

# 

@register.simple_tag
def generate_lottie_animation(animation_name, container_id):
    json_path = f"{settings.STATIC_URL}animations/{animation_name}.json"
    return format_html(
        '<div id="{container_id}" class="lottie-animation"></div>'
        '<script>'
        '   const animationContainer = document.getElementById("{container_id}");'
        '   if (animationContainer) {{'
        '       const animation = lottie.loadAnimation({{'
        '           container: animationContainer,'
        '           renderer: "svg",'
        '           loop: true,'
        '           autoplay: true,'
        '           path: "{json_path}",'
        '       }});'
        '   }} else {{'
        '       console.error("Container not found:", "{container_id}");'
        '   }}'
        '</script>',
        container_id=container_id,
        json_path=json_path,
    )
