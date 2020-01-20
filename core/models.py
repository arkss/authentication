from django.conf import settings
from django.db import models
import os
from hashlib import md5, sha256

class Profile(models.Model):
    username = models.CharField(max_length=30)
    # encrypt(password + salt)
    password = models.CharField(max_length=64)
    name = models.CharField(max_length=20)
    gender = models.CharField(choices=[('man', '남성'),('woman', '여성')] ,max_length=5)
    email = models.EmailField()


    def __str__(self):
        return self.name


    def set_hash_password(self, row_password):
        salt = md5(os.urandom(32)).hexdigest()
        Salt.objects.create(value = salt)
        hashed_password = sha256((salt + row_password).encode('utf8')).hexdigest()
        
        self.password = hashed_password


class Salt(models.Model):
    value = models.CharField(max_length=32)

    def __str__(self):
        return self.value

