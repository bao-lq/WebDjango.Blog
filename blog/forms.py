from django import forms
from .models import Comment, Post
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)

    def save(self, commit = True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.post = self.post
        comment.save()
    
    class Meta:
        model = Comment
        fields = ["body"]

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['author'].queryset = User.objects.filter(pk=user.pk)
        
    class Meta:
        model = Post
        fields = '__all__'