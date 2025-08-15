from django.shortcuts import render , HttpResponse ,redirect , get_object_or_404
from django.http import HttpResponseNotFound
from .models import Women , Category , TagPost

menu = [
    {"title": "About", "url_name": "about"},
    {"title": "Add Page", "url_name": "addpage"},
    {"title": "Contact", "url_name": "contact"},
    {"title": "Login", "url_name": "login"}
]

def index(request):
    posts = Women.published.all().select_related()
    data = {
                'menu':menu,
                'title':'Main page',
                'posts':posts ,
                'cat_selected':0
            }
    return render(request,'main/index.html', data)


def show_post(request,post_slug):
    post = get_object_or_404(Women,slug=post_slug)
    data = {'menu':menu,
            'title':post.title,
            'post': post,
            'cat_selected':0
            }
    return render(request,'main/post.html',data)

def about(request):
    data = {'menu':menu,'title':'About us'}
    return render(request,'main/about.html',data)
    
def addpage(request):
    return HttpResponse('Add article')

def contact(request):
    return HttpResponse('Call back')

def login(request):
    return HttpResponse('Login')

def show_category(request,cat_slug):
    category = get_object_or_404(Category,slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')
    data = {'menu':menu,'title':f'Category {category.name}','posts': posts,'cat_selected':cat_slug}
    return render(request,'main/index.html',data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")

def show_tag_post_list(request,tag_slug):
    tag = get_object_or_404(TagPost,slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')
    data = {'menu':menu,'title':f'Tag {tag.tag}','posts': posts,'cat_selected':None}

    return render(request,'main/index.html',context=data)
