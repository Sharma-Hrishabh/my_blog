from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank='True')
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)



    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + '...'


class Comment(models.Model):
    article = models.ForeignKey('Articles', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
