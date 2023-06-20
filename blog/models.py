from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'id: ' + str(self.id) + ' title: ' + self.title + '\n'
        # return self.title

class login(models.Model):
    account = models.TextField()
    password = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'id: ' + str(self.id) + ' title: ' + self.account + '\n'