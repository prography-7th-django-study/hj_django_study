from django.db import models
from profiles.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='board', blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    members = models.ManyToManyField(
        Profile,
        through='members.Member',
        through_fields=('post', 'member'),)

class Comment(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    description = models.TextField()
    parent = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)