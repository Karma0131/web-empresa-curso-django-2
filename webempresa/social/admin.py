from typing import Any, List, Optional, Tuple, Union
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):

        if request.user.groups.filter(name='Personal').exists():
            return ('created', 'updated', 'key', 'name')
        
        else:
            return ('created', 'updated')

        pass


admin.site.register(Link, LinkAdmin)

'''class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display=('title', 'author','published','post_categories')
    ordering=('author','published')
    search_fields=('title','content','author__username', 'categories__name')
    date_hierarchy='published'
    list_filter=('author__username','categories__name')

    def post_categories(self,obj):
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description='Categorias'
    
admin.site.register(Post, PostAdmin)'''
