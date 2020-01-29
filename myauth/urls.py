from django.urls import path
from .views import *
from . import views

app_name = 'myauth'

urlpatterns = [
    path('main/', main, name="main"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('sign_up/', CreateUserView.as_view(), name="sign_up"),
    path('find_id/', find_id, name="find_id"),
    path('find_password/', find_password, name="find_password"),
    path('change_password/<str:uuid>/',
         change_password, name="change_password"),
    path('id_overlap_check/', id_overlap_check, name="id_overlap_check"),
    path('user_activate/<str:uuid>', user_activate, name="user_activate")
]
