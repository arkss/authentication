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


@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny] 
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def post(self, request, *args, **kargs):
        print(request.headers)
        user = request.data.get('user')
        if not user:
            return Response({'response': 'error', 'message': 'No data found'})
        
        serializer = UserSerializerWithToken(data=user)
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            print(serializer.errors)
            return Response({'response': 'error', 'message': serializer.errors})
        return Response({'response': 'success', 'message': 'user create sucessfully'})

    def get(self, request, *args, **kargs):
        return Response(template_name='myauth/sign_up.html')

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny] 
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)
    
    #TODO login 과 signup 이 각각 fake button click, submit 이벤트여서 request 넘어보는 값이 다르다. 
    def post(self, request, *args, **kargs):
        print(request.headers)
        print(request.accepted_renderer.format)
        username = request.data['username']
        password = request.data['password']

        # if not user:
        #     return Response({
        #         'response': 'error',
        #         'message': 'No data found'
        #     })
        user = MyUser.objects.get(username=username)

        if check_password(password, user.password):
            # 토큰을 발급받는다
            print("비밀번호 확인")

            return Response({
                'response': 'success',
                'message': '로그인이 성공적으로 수행되었습니다.'
            })
        else:
            print("비밀번호 미확인")
            return Response({
                'response': 'error',
                'message': '존재하지 않는 사용자입니다.'
            })

    def get(self, request, *args, **kargs):
        return Response(template_name='myauth/login.html')




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
