from django.contrib import admin
from .models import MyUser, Salt

admin.site.register(MyUser)
admin.site.register(Salt)