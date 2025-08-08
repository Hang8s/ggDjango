from django.urls import path ,re_path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('cats/<int:cat_id>/',views.categories,name='cats_id'),
    path('cats/<slug:cat_slug>/',views.categories_by_slug,name='cats'),
]
