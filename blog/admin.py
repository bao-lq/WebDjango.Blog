from django.contrib import admin
from .models import Post, Comment
from django.contrib.admin.actions import delete_selected

class CommentInline(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'date']
    list_filter = ['date']
    search_fields = ['title']
    inlines = [CommentInline]
    actions = ['delete_model']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def delete_model(self, request, obj):
        for o in obj.all():
            o.delete()
    delete_model.short_description = 'Delete selected'

# Register your models here.
admin.site.register(Post, PostAdmin)