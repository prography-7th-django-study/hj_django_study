from django.db import models
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver
from accounts.models import User
from posts.models import Post, Comment, Member


class Notification(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    messages = models.CharField(max_length=32)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

@receiver(post_save, sender=User)
def create_user_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance, messages="가입을 축하합니다.")

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.post.author, messages="새로운 댓글이 달렸습니다.")

@receiver(post_save, sender=Member)
def create_member_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.post.author, messages="새로운 가입신청이 왔습니다.")

@receiver(post_delete, sender=Member)
def delete_member_notification(sender, instance, **kwargs):
    Notification.objects.create(user=instance.member, messages="가입이 거부당하셨습니다.")

@receiver(post_save, sender=Member)
def change_member_notification(sender, instance, **kwargs):
    if instance.is_dirty:
        Notification.objects.create(user=instance.member, messages="가입이 수락되었습니다.")