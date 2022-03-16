from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from config import settings


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, password, description, image):

        if not email:
            raise ValueError('must have user email')
        if not nickname:
            raise ValueError('must have user nickname')
        if not password:
            raise ValueError('must have user password')

        user = self.model(
            email=email,
            nickname=nickname,
            description=description,
            image=image,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, nickname, password=None, description=None, image=None, **kwargs):

        user = self.create_user(
            email = email,
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
    email = models.EmailField(max_length=255,unique=True,)
    nickname = models.CharField(max_length=16, unique=True)
    image = models.ImageField(upload_to='profile', blank=True, default='')
    description = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']
    def __str__(self):
        return self.nickname

    @property
    def is_staff(self):
        return self.is_admin
