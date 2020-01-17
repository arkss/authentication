from django.contrib import admin
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('main/', views.main, name="main"),
    path('', views.login, name="login"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('find_id/', views.find_id, name="find_id"),
    path('find_password/', views.find_password, name="find_password"),
    path('id_overlap_check/', views.id_overlap_check, name="id_overlap_check"),
]
