from django.db import models

class Salt(models.Model):
    value = models.CharField(max_length=32)

    def __str__(self):
        return self.value

