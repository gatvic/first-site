from django.contrib import admin
from .models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'slug', 'published_date', 'cat')
    list_display_links = ('author', 'title', 'text')
    search_fields = ('author', 'title', 'text')


admin.site.register(Post, PostAdmin)

admin.site.register(Cat)
