from django import template
from django.db.models import Count
from main.models import Category, TagPost

register = template.Library()

@register.inclusion_tag('main/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total_posts=Count('posts')).filter(total_posts__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('main/list_tags.html')
def show_all_tags(cat_selected=0):
    tags = TagPost.objects.annotate(total_tags=Count('tags')).filter(total_tags__gt=0)
    return {'tags': tags}
