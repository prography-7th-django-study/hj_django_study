from django.db import models
from django.utils.translation import gettext_lazy as _

class Member(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    member = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)

    class IsMember(models.TextChoices):
        CONFIRMED = 'Co', _('Confirmed')
        PENDED = 'Pe', _('Pended')

    is_member = models.CharField(
        max_length=2,
        choices=IsMember.choices,
        default=IsMember.PENDED,
    )
