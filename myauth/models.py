from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import os
from hashlib import md5, sha256


class MyUser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username

    def set_password(self, user_id, row_password):
        salt = md5(os.urandom(32)).hexdigest()
        salt_obj = Salt(
            user_id = user_id,
            value = salt
        )
        salt_obj.save()
        hashed_password = sha256((salt + row_password).encode('utf8')).hexdigest()

        self.password= hashed_password


class Salt(models.Model):
    user_id = models.IntegerField()
    value = models.CharField(max_length=32)


    def __str__(self):
        return self.value