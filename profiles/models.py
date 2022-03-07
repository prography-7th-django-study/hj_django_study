from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User

class Profile(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=50, unique=True, blank=True, default='')
    image = models.ImageField(upload_to='profile', blank=True, default='')
    description = models.TextField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()