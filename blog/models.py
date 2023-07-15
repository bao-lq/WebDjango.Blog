from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,)
    body = models.TextField()
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'id: ' + str(self.id) + ' title: ' + self.title + '\n'
        # return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)