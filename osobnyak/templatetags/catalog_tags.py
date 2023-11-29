from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.tag(name="catalog_item")
def catalog_item(parser, token):
    return render_to_string(template_name='catalog-item.html',
                            context={'items': items})
