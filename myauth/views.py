from .serializers import GetFullUserSerializer, UserSerializerWithToken
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import permissions
from django.http import JsonResponse
from django.shortcuts import render
from .models import MyUser


@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny] 
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

    def post(self, request):
        user = request.data.get('user')
        if not user:
            return Response({'response': 'error', 'message': 'No data found'})
        
        serializer = UserSerializerWithToken(data=user)
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({'response': 'error', 'message': serializer.errors})
        return Response({'response': 'success', 'message': 'user create sucessfully'})

    def get(self, request):
        return Response(template_name='myauth/sign_up.html')

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny] 
    renderer_classes = [TemplateHTMLRenderer]
    
    def get(self, request, *args, **kwargs):
        return Response(template_name='myauth/login.html')

    def post(self, request):
        pass


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
