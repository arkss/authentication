from django.contrib import admin
from .models import Profile, Salt

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'gender', 'email']
    search_fields = ['username']
    
admin.site.register(Salt)
