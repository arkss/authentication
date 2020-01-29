from django.contrib import admin
from .models import MyUser, Salt


@admin.register(MyUser)
class MyUserAmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active']
