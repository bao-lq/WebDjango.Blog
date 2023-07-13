from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInline]

# Register your models here.
admin.site.register(Post, PostAdmin)