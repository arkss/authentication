from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),

    path('token-auth/', obtain_jwt_token),
    path('', include('myauth.urls')),

]
