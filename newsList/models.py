from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=120)
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content