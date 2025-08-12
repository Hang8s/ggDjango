from django.shortcuts import render , HttpResponse ,redirect , get_object_or_404
from django.http import HttpResponseNotFound
from .models import Women , Category

menu = [
    {"title": "About", "url_name": "about"},
    {"title": "Add Page", "url_name": "addpage"},
    {"title": "Contact", "url_name": "contact"},
    {"title": "Login", "url_name": "login"}
]

cats_db =[
    {'id':1,'name':'Actress'},
    {'id':2,'name':'Singers'},
    {'id':3,'name':'Sportguys'},
]


def index(request):
    posts = Women.published.all()
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
    posts = Women.published.filter(cat_id=category.pk)
    data = {'menu':menu,'title':f'Category {category.name}','posts': posts,'cat_selected':cat_slug}
    return render(request,'main/index.html',data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
