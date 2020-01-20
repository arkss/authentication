from django.conf import settings
from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=30)
    # encrypt(password + salt)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    gender = models.CharField(choices=[('man', '남성'),('woman', '여성')] ,max_length=5)
    email = models.EmailField()
    
    def __str__(self):
        return self.name