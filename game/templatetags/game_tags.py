from django import template
from game.models import *

register = template.Library()

@register.simple_tag(name='getcategories')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('game/list_categories.html')
def show_categories(sort=None, category_selected=0):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)

    return {'categories': categories, 'category_selected': category_selected}