from django.db import models
from django.utils.translation import gettext_lazy as _

class Member(models.Model):
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
