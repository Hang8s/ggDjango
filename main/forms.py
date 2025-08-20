from django import forms
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

from .models import Category,Husband,Women

@deconstructible
class UkrValidator():
    ALLOWED_CHARS = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ "
    code = 'ua'

    def __init__(self,message=None):
        self.message = message if message else 'Can be only ua syblols - and space '
    def __call__(self,value,*args,**kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message,code=self.code)

# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255,min_length=5,label='Title'error_messages={'min_length':'To short title'},widget=forms.TextInput(attrs={'class': 'form-input','required':'you need title!'}))
#     slug = forms.SlugField(max_length=255,label='Url',validators=[MinLengthValidator(5),MaxLengthValidator(100)])
#     content = forms.CharField(required=False,widget=forms.Textarea(attrs={'cols':50,'rows':5}),label='Content')
#     is_published = forms.BooleanField(required=False,label='Publish',initial=True)
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label="Category not selected",label='Category')
#     husband = forms.ModelChoiceField(queryset=Husband.objects.all(),required=False,empty_label='Single',label='Husband')


#     def clean_title(self):
#         title =self.cleaned_data
#         ALLOWED_CHARS = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ "
#         if not (set(title) <= set(ALLOWED_CHARS)):
#             raise ValidationError('Can be only ua syblols - and space ')
        
class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label="Category not selected",label='Category')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(),required=False,empty_label='Single',label='Husband')

    class Meta:
        model = Women
        fields='__all__'
        widgets ={
            'title':forms.TextInput(attrs={'class': 'form-input','required':'you need title!'}),
            'content':forms.Textarea(attrs={'cols': 50,'rows':5})
        }
        labels  ={
            'slug':'Url'
        }

    def clead_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("to long")
        
        return title
    
class UploadFileForm(forms.Form):
    file = forms.ImageField(label='File')