from django.db import models
from django.contrib.auth.models import User


class NewsType(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    subscription = models.ManyToManyField(NewsType, related_name="subscription_type")

    def __str__(self):
        return self.user.username


class MagicNews(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    type = models.OneToOneField(NewsType, on_delete=models.CASCADE, related_name='news_type')
    image = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
