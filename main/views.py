from django.shortcuts import render , HttpResponse ,redirect
from django.http import HttpResponseNotFound

menu = ['about us', 'Add article','Call back', ' Log in']

# Create your views here.
def index(request):
    data = {'menu':menu,'title':'Main page'}
    return render(request,'main/index.html', data)

def about(request):
    data = {'menu':menu,'title':'About us'}
    return render(request,'main/about.html',data)
    
def categories(request,cat_id):
    if cat_id > 1000:
        return redirect('cats','musick')
    return HttpResponse(f"<h1>Acrticles</h1><p>id:{cat_id}</p>")

def categories_by_slug(request,cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Acrticles</h1><p>slug:{cat_slug}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
