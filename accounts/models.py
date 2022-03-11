from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, nickname, password, description, image):

        if not nickname:
            raise ValueError('must have user nickname')
        if not password:
            raise ValueError('must have user password')

        user = self.model(
            nickname=nickname,
            description=description,
            image=image,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, password=None, description=None, image=None, **kwargs):

        user = self.create_user(
            nickname=nickname,
            description='',
            image='',
            password = password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    nickname = models.CharField(max_length=16, unique=True, blank=True, default='')
    image = models.ImageField(upload_to='profile', blank=True, default='')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'nickname'

    def __str__(self):
        return self.nickname

    @property
    def is_staff(self):
        return self.is_admin