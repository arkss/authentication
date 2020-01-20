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


    def set_hash_password(self, profile_id, row_password):
        salt = md5(os.urandom(32)).hexdigest()
        salt_obj = Salt(
            profile_id=profile_id,
            value = salt
        )
        salt_obj.save()
        hashed_password = sha256((salt + row_password).encode('utf8')).hexdigest()
        
        self.password = hashed_password

    
    def authenticate(self, salt, row_password):
        hashed_password = sha256((salt + row_password).encode('utf8')).hexdigest()

        return self.password == hashed_password




class Salt(models.Model):
    profile_id = models.IntegerField()
    value = models.CharField(max_length=32)


    def __str__(self):
        return self.value
