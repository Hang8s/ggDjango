from django.shortcuts import render , HttpResponse ,redirect
from django.http import HttpResponseNotFound

menu = [
    {"title": "About", "url_name": "about"},
    {"title": "Add Page", "url_name": "addpage"},
    {"title": "Contact", "url_name": "contact"},
    {"title": "Login", "url_name": "login"}
]

data_db = [
    {
        "id": 1,
        "title": "Taylor Swift",
        "content": (
            "American singer-songwriter and global pop icon. Known for her narrative songwriting "
            "that often centers around her personal life. Winner of multiple Grammy Awards and "
            "Billboard recognitions. Taylor has influenced millions of fans worldwide with her "
            "unique style, blending country, pop, and indie genres. She is also a strong advocate "
            "for artists' rights and social causes."
        ),
        "is_active": True
    },
    {
        "id": 2,
        "title": "Emma Watson",
        "content": (
            "British actress and activist famous for playing Hermione Granger in the Harry Potter series. "
            "Emma is also a passionate advocate for gender equality and women’s rights, serving as a UN Women Goodwill Ambassador. "
            "She has a degree in English literature and has spoken at the United Nations on feminism and education. "
            "Besides acting, she supports sustainable fashion and humanitarian causes globally."
        ),
        "is_active": True
    },
    {
        "id": 3,
        "title": "Priyanka Chopra",
        "content": (
            "Indian actress, singer, and former Miss World 2000. Priyanka has become a major figure in Bollywood and Hollywood. "
            "She is known for her versatile acting, dancing skills, and philanthropic work. Chopra supports education for girls "
            "and has been involved in UNICEF campaigns. She is also a producer and has several successful TV and film projects worldwide."
        ),
        "is_active": True
    },
    {
        "id": 4,
        "title": "Beyoncé Knowles",
        "content": (
            "American singer, songwriter, and performer widely regarded as one of the greatest entertainers of all time. "
            "Beyoncé rose to fame with Destiny's Child and has released numerous chart-topping solo albums. "
            "She is also known for her powerful voice, dynamic performances, and activism for racial equality and women's empowerment. "
            "Her influence extends beyond music into fashion, film, and philanthropy."
        ),
        "is_active": True
    },
    {
        "id": 5,
        "title": "Gal Gadot",
        "content": (
            "Israeli actress, model, and former Miss Israel 2004. Gal gained worldwide fame for her role as Wonder Woman in the DC Extended Universe. "
            "Before acting, she served two years in the Israeli Defense Forces. Gadot is admired for her strong, empowering roles and humanitarian efforts. "
            "She actively promotes women's rights and is involved in various charitable organizations."
        ),
        "is_active": True
    },
    {
        "id": 6,
        "title": "Rihanna Fenty",
        "content": (
            "Barbadian singer, businesswoman, and fashion icon known for her versatile music style and bold persona. "
            "Rihanna has released multiple multi-platinum albums and won numerous awards. "
            "She founded Fenty Beauty, which is praised for its inclusivity across skin tones. "
            "Rihanna is also a philanthropist, supporting education, health, and emergency response initiatives worldwide."
        ),
        "is_active": True
    },
    {
        "id": 7,
        "title": "Adele Adkins",
        "content": (
            "British singer known for her soulful voice and emotional ballads. Adele has won numerous Grammy Awards and an Academy Award. "
            "Her albums have sold millions globally, making her one of the best-selling music artists. "
            "She is praised for her powerful vocal performances and heartfelt songwriting. "
            "Adele also advocates for mental health awareness and body positivity."
        ),
        "is_active": True
    },
    {
        "id": 8,
        "title": "Lupita Nyong'o",
        "content": (
            "Kenyan-Mexican actress and advocate for diversity and inclusion in Hollywood. "
            "Lupita won an Academy Award for her role in '12 Years a Slave'. "
            "She is also known for her activism on racial equality and women empowerment. "
            "Besides acting, Lupita is a published author and frequently speaks about representation and self-love."
        ),
        "is_active": True
    },
]

cats_db =[
    {'id':1,'name':'Actress'},
    {'id':2,'name':'Singers'},
    {'id':3,'name':'Sportguys'},
]


def index(request):
    data = {'menu':menu,'title':'Main page','posts': data_db,'cat_selected':0}
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

def show_category(request,cat_id):
    data = {'menu':menu,'title':'Show by category','posts': data_db,'cat_selected':cat_id}
    return render(request,'main/index.html',data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
