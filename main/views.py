from django.shortcuts import render , HttpResponse ,redirect
from django.http import HttpResponseNotFound

menu = [
    {"name": "About", "url_name": "about"},
    {"name": "Add Page", "url_name": "addpage"},
    {"name": "Contact", "url_name": "contact"},
    {"name": "Login", "url_name": "login"}
]

data_db = [
    {"id": 1, "name": "Laptop", "desc": "Portable computer for work and gaming", "is_published": True},
    {"id": 2, "name": "Phone", "desc": "Smartphone with high-resolution camera", "is_published": True},
    {"id": 3, "name": "Tablet", "desc": "Touchscreen device for browsing and media", "is_published": False},
    {"id": 4, "name": "Headphones", "desc": "Wireless over-ear headphones with noise canceling", "is_published": True},
    {"id": 5, "name": "Smartwatch", "desc": "Wearable device for fitness and notifications", "is_published": False},
    {"id": 6, "name": "Camera", "desc": "Professional DSLR camera for photography", "is_published": True}
]

def index(request):
    data = {'menu':menu,'title':'Main page','posts':data_db}
    return render(request,'main/index.html', data)


def show_post(request,post_id):
    return HttpResponse(f"Show post with id:{post_id}")

def about(request):
    data = {'menu':menu,'title':'About us'}
    return render(request,'main/about.html',data)
    
def addpage(request):
    return HttpResponse('Add article')

def contact(request):
    return HttpResponse('Call back')

def login(request):
    return HttpResponse('Login')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
