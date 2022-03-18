from dirtyfields import DirtyFieldsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='post', blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='related_posts')
    members = models.ManyToManyField(
        'accounts.User',
        through='posts.Member',
        through_fields=('post', 'member'),)
    # mebers필드의 경우 post와 member가 있어야 참조가 가능하기때문에 migrations 진행시 members 필드 뺀상태로 migrations 이후 members 포함시킨뒤 migrations을 총 2번적용시켜야함!

    @property
    def comment_count(self):
        return self.comment_set.count()

    @property
    def member_count(self):
        return self.member_set.count()

    class Meta:
        ordering = ['-id']

@receiver(post_save, sender=Post)
def create_post_member(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(post=instance, member=instance.author, member_type='Co')


class Comment(models.Model):
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    description = models.TextField()
    parent = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, blank=True, default='', null=True)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']


class Member(models.Model, DirtyFieldsMixin):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    member = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    class MemberType(models.TextChoices):
        CONFIRMED = 'Co', _('Confirmed')
        PENDED = 'Pe', _('Pended')

    member_type = models.CharField(
        max_length=2,
        choices=MemberType.choices,
        default=MemberType.PENDED,
    )

    class Meta:
        ordering = ['-id']
