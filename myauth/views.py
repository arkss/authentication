from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import permissions
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.hashers import check_password
from .models import MyUser, Salt
from .serializers import GetFullUserSerializer, UserSerializerWithToken
# jwt
import jwt
from datetime import datetime
from django.conf import settings

@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny] 
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def post(self, request, *args, **kargs):
        user = request.data.get('user')
        if not user:
            return Response({'response': 'error', 'message': 'No data found'})
        
        serializer = UserSerializerWithToken(data=user)
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({'response': 'error', 'message': serializer.errors})
        return Response({'response': 'success', 'message': 'user create sucessfully'})

    def get(self, request, *args, **kargs):
        return Response(template_name='myauth/sign_up.html')

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny] 
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
    
    #TODO login 과 signup 이 각각 fake button click, submit 이벤트여서 request 넘어보는 값이 다르다. 
    def post(self, request, *args, **kargs):
        user = request.data.get('user')

        if not user:
            return Response({
                'response': 'error',
                'message': 'No data found'
            })

        username = user['username']
        password = user['password']
        
        user = MyUser.objects.get(username=username)

        if check_password(password, user.password):
            jwt_token = jwt_create(username)
            cache.set('jwttoken',jwt_token)
            print(cache.get('jwttoken'),"@@@@@@@@@")
            response = Response({
                'response': 'success',
                'message': 'sucess login',
            })
            response.set_cookie('jwttoken', jwt_token)
            return response
        else:
            return Response({
                'response': 'error',
                'message': 'password is wrong'
            })

    def get(self, request, *args, **kargs):
        return Response(template_name='myauth/login.html')



def jwt_create(username):
    now = datetime.now()
    key = settings.SECRET_KEY
    now_time = str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)
    payload = {
        "username": username,
        "now_time": now_time
    }
    jwt_token = jwt.encode(payload, key, algorithm='HS256').decode('utf-8')
    return jwt_token

def main(request):
    return render(request, 'myauth/main.html')


def login(request):
    return render(request, 'myauth/login.html')


def sign_up(request):
    return render(request, 'myauth/sign_up.html')


def find_id(request):
    pass


def find_password(request):
    pass

def id_overlap_check(request):
    username = request.GET.get('username')

    try:
        user = MyUser.objects.get(username=username)
    except:
        user = None
    overlap = "pass" if user is None else "fail"
    context = {
        'overlap': overlap,
    }
    return JsonResponse(context)

from django.core.cache import cache

def redis_test(request):

    users = cache.get_or_set('users',MyUser.objects.all().values('username'))

    return JsonResponse(list(users),safe=False)