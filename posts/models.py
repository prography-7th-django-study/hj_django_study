from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from members.models import Member
from profiles.models import Profile


class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='post', blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='posted_author')
    members = models.ManyToManyField(
        Profile,
        through='members.Member',
        through_fields=('post', 'member'),)

@receiver(post_save, sender=Post)
def create_post_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(post=instance, member=instance.author, is_member='Co')


class Comment(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    description = models.TextField()
    parent = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, blank=True, default='', null=True)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)