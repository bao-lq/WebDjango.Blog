from django.db import models
from django.conf import settings
from django.urls import reverse
from django import forms

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to = "images/")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'id: ' + str(self.id) + ' title: ' + self.title + '\n'
        # return self.title
    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)