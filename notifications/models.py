from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from posts.models import Comment


class Notification(models.Model):
    user = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    messages = models.CharField(max_length=32)
    status = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance, messages="가입을 축하합니다.")