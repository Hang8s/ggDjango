from django.contrib import admin , messages
from .models import Women ,Category

class MarriedFilter(admin.SimpleListFilter):
    title = 'Women Status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married','Married'),
            ('single','Single')
        ]
    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull =False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull =True)

# Register your models here.
@admin.register(Women)
class Womenadmin(admin.ModelAdmin):
    fields = ['title','content','slug','cat','husband','tags']
    prepopulated_fields = {'slug':('title',)}
    filter_horizontal = ['tags']
    list_display = ('title','time_created','is_published','cat','brief_info')
    list_display_links =('title',)
    ordering = ['time_created','title']

    list_editable =['is_published']
    list_per_page=10

    search_fields = ['title','cat__name']
    list_filter = ['cat__name','is_published',MarriedFilter]

    actions = ['set_published','set_draft']

    @admin.display(description='Short description',ordering='content')
    def brief_info(self,women:Women):
        return f'Description {len(women.content)} symbols'
    
    def set_published(self,request,queryset):
        count = queryset.update(is_published = Women.Status.PUBLISHED)
        self.message_user(request,f'Redacted {count} notes')

    def set_draft(self,request,queryset):
        count = queryset.update(is_published = Women.Status.DRAFT)
        self.message_user(request,f'Redacted {count} notes',messages.WARNING)
# admin.site.register(Women,Womenadmin)

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links =('id','name')

