from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    gender = models.CharField(choices=[('man', '남성'),('woman', '여성')] ,max_length=5)
    email = models.EmailField()

    def __str__(self):
        return self.name