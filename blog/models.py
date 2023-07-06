from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'id: ' + str(self.id) + ' title: ' + self.title + '\n'
        # return self.title