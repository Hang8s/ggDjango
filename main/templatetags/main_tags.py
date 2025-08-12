from django import template
import main.views as views
from main.models import Category

register = template.Library()


@register.inclusion_tag('main/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats':cats,'cat_selected':cat_selected}