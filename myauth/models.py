from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import os
from hashlib import md5, sha256


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError('must have user email')
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.role = "0"
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('0', '일반 유저'),
        ('5', '세탁소 사장'),
        ('10', '관리자')
    )
    objects = UserManager()

    email = models.EmailField(
        max_length=255,
    )
    username = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    role = models.CharField(max_length=2, choices=ROLE_CHOICES)

    #is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    @property
    def is_staff(self):
        return self.role == "0"

    @property
    def is_superuser(self):
        return self.role == "0"


class Salt(models.Model):
    user_id = models.IntegerField()
    value = models.CharField(max_length=32)

    def __str__(self):
        return self.value
