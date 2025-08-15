from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

# def translit_to_eng(s:str):
#     d = {
#     'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g',
#     'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z',
#     'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k',
#     'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
#     'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
#     'ь': '', 'ю': 'iu', 'я': 'ia',
#     }
#     return ''.join(d.get(char, char) for char in s.lower())


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)

class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0 , 'draft'
        PUBLISHED = 1, 'Published'
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,unique=True,db_index=True,blank=True)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=[(True, "Published"), (False, "Draft")],default=True)
    cat = models.ForeignKey('Category',on_delete=models.PROTECT,related_name='posts')
    tags = models.ManyToManyField('TagPost',blank=True,related_name='tags')
    husband = models.OneToOneField('Husband',blank=True,on_delete=models.SET_NULL,null=True,related_name='wife')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Popular women'
        verbose_name_plural = 'Popular womens'
        ordering = ['-time_created']
        indexes =[
            models.Index(fields=['-time_created'])
        ]

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})
    
    # def save(self,*args,**kwargs):
    #     self.slug = slugify(translit_to_eng(self.title))
    #     super().save(*args,**kwargs)

    
class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category',kwargs={'cat_slug':self.slug})
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class TagPost(models.Model):
    tag = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True)

    def __str__(self):
        return self.tag
    
    def get_absolute_url(self):
        return reverse('tag',kwargs={'tag_slug':self.slug})
    
class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.name