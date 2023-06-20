from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'date']
    list_filter = ['date']
    search_fields = ['title']

# Register your models here.
admin.site.register(Post, PostAdmin)