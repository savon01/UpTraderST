from django import template
from menu_app.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path

    menu = Menu.objects.get(name=menu_name)
    menu_items = menu.get_descendants(include_self=True)

    return {
        'menu_items': menu_items,
        'current_url': current_url,
    }
