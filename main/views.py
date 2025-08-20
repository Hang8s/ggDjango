from django.shortcuts import render , HttpResponse ,redirect , get_object_or_404
from django.http import HttpResponseNotFound
from .models import Women , Category , TagPost , UploadFiles
from .forms import AddPostForm, UploadFileForm

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

# def handle_uploaded_file(f):
#     with open(f"uploads/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request):
    if request.method == 'POST' and 'file' in request.FILES:
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(form.cleaned_data['file'])
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()

    else:
        form = UploadFileForm()
    data = {'menu': menu, 'title': 'About us','form':form}
    return render(request, 'main/about.html', data)

def addpage(request):
    if request.method == 'POST' :
        form = AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # try:
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(None, "Error creating post")
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    data = {
        'menu':menu,
        'title':'Add page',
        'form':form 
    }
    return render(request,'main/addpage.html',data)

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
