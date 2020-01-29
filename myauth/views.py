from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework import permissions
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import MyUser, Salt
from .serializers import UserSerializer
# jwt
import jwt
from datetime import datetime
from django.conf import settings
# mail 인증
from uuid import uuid4
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.views.decorators.csrf import csrf_exempt


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def post(self, request, *args, **kargs):
        user = request.data.get('user')
        if not user:
            return Response({
                'response': 'error',
                'message': 'No data found'
            })
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            user = serializer.save()
        else:
            return Response({
                'response': 'error',
                'message': serializer.errors
            })

        uuid = uuid4()
        cache.set(uuid, user.id)
        current_site = get_current_site(request)
        mail_content = render_to_string(
            'myauth/user_activate_email.html',
            {
                'domain': current_site.domain,
                'uuid': uuid
            }
        )
        mail_subject = "회원가입 인증 메일입니다."
        email = EmailMessage(mail_subject, mail_content, to=[user.email])
        email_result = email.send()
        if email_result == 1:
            message = "이메일이 성공적으로 전송되었습니다."
        else:
            message = "이메일이 전송에 실패하였습니다."
        return Response({
            "response": "success",
            "message": message
        })

    def get(self, request, *args, **kargs):
        return Response(template_name='myauth/sign_up.html')


class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)

    # TODO login 과 signup 이 각각 fake button click, submit 이벤트여서 request 넘어보는 값이 다르다.
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

        if not user.is_active:
            return Response({
                'response': 'error',
                'message': '이메일 인증이 완료되지 않았습니다.'
            })

        if check_password(password, user.password):
            jwt_token = jwt_create(username)
            cache.set('jwttoken', jwt_token)
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
    now_time = str(now.year)+str(now.month)+str(now.day) + \
        str(now.hour)+str(now.minute)+str(now.second)
    payload = {
        "username": username,
        "now_time": now_time
    }
    jwt_token = jwt.encode(payload, key, algorithm='HS256').decode('utf-8')
    return jwt_token


@api_view(['POST', 'GET'])
@permission_classes([permissions.AllowAny])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, ])
def find_password(request):
    if request.method == "POST":
        username = request.data.get('username')
        user = MyUser.objects.get(username=username)

        uuid = uuid4()
        cache.set(uuid, user.id)
        current_site = get_current_site(request)
        mail_content = render_to_string(
            'myauth/find_password_email.html',
            {
                'domain': current_site.domain,
                'username': username,
                'uuid': uuid
            }
        )
        mail_subject = "비밀번호 변경 메일입니다."
        email = EmailMessage(mail_subject, mail_content, to=[user.email])
        email_result = email.send()
        return Response({
            'response': 'success',
            'message': '메일이 성공적으로 보내졌습니다.'
        })

    else:
        return Response(template_name='myauth/find_password.html')


@api_view(['POST', 'GET'])
@permission_classes([permissions.AllowAny])
@renderer_classes([TemplateHTMLRenderer, JSONRenderer, ])
def change_password(request, uuid):
    if request.method == 'POST':
        password = request.data.get('password')
        check_password = request.data.get('check_password')
        if password == check_password:
            user_id = cache.get(uuid)
            user = MyUser.objects.get(id=user_id)
            user.set_password(password)
            user.save()
            return Response({
                'response': 'success',
                'message': '비밀번호가 변경되었습니다.'
            })
        else:
            return Response({
                'response': 'error',
                'message': '입력한 비밀번호가 다릅니다.'
            })
    else:
        context = {
            'uuid': uuid
        }
        return Response(context, template_name='myauth/change_password.html')


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


def user_activate(request, uuid):
    user_id = cache.get(uuid)
    if user_id is None:
        messages.info(request, "인증이 만료되었습니다.")
        redirect('myauth:login')

    user = MyUser.objects.get(id=user_id)

    if user is not None:
        user.is_active = True
        user.save()
        messages.info(request, "메일 인증이 완료되었습니다.")
    else:
        messages.info(request, "해당 유저가 존재하지 않습니다.")

    return redirect('myauth:login')


@api_view(['GET', ])
def main(request):
    return Response(template_name='myauth/main.html')


def find_id(request):
    pass
