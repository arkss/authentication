from django.urls import path
from .views import *
from . import views

app_name = 'myauth'

urlpatterns = [
    path('current_user/', get_current_user, name="get_current_user"),
    

    path('main/', main, name="main"),
    path('login/', UserLoginView.as_view()),
    path('sign_up/',CreateUserView.as_view(), name="sign_up"),
    path('find_id/', find_id, name="find_id"),
    path('find_password/', find_password, name="find_password"),
    path('id_overlap_check/', id_overlap_check, name="id_overlap_check"),
]


