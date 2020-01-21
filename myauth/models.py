from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import os
from hashlib import md5, sha256



class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def create_user(self, email, username, password=None):        
        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            username = username        
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user     
    def create_superuser(self, email, username,password ):        
       
        user = self.create_user(            
            email = self.normalize_email(email),            
            username = username,            
            password=password        
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 


class MyUser(AbstractBaseUser,PermissionsMixin):    
    
    objects = UserManager()
    
    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )    
    username = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )     
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'username'    
    REQUIRED_FIELDS = ['email']






# class MyUser(models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=64)

#     def __str__(self):
#         return self.username

    # def set_password(self, row_password):
    #     salt = md5(os.urandom(32)).hexdigest()
    #     salt_obj = Salt(
    #         user_id = self.id,
    #         value = salt
    #     )
    #     salt_obj.save()
    #     hashed_password = sha256((salt + row_password).encode('utf8')).hexdigest()

    #     self.password = hashed_password

    # def authenticate(self, salt, row_password):
    #     hashed_password = sha256((salt + row_password).encode('utf8')).hexdigest()

    #     return self.password == hashed_password



class Salt(models.Model):
    user_id = models.IntegerField()
    value = models.CharField(max_length=32)


    def __str__(self):
        return self.value