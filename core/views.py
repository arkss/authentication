from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth, messages
from .models import Profile

def main(request):
    return render(request, 'core/main.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if user is not None:
            auth.login(request, user)
        else:
            messages.error(request, "입력한 아아디와 비밀번호를 다시 확인해주세요.")
            return redirect('core:login')

    return render(request, 'core/login.html')


def sign_up(request):
    if request.method == 'POST':
        password = request.POST.get('password1')
        check_password = request.POST.get('password2')
        if password == check_password:
            username = request.POST['username']
            name = request.POST['name']
            gender = request.POST['gender']
            email = request.POST['email']

            profile = Profile(
                username=username,
                name=name,
                gender=gender,
                email=email
            )
            profile.set_hash_password(password)
            profile.save()
            return redirect('core:main')
        else:
            messages.error(request, "비밀번호가 일치하지 않습니다.")
            return redirect('core:sign_up')
    else:
        return render(request, 'core/sign_up.html')


def find_id(request):
    pass


def find_password(request):
    pass


def id_overlap_check(request):
    username = request.GET.get('username')

    try:
        user = User.objects.get(username=username)
    except:
        user = None

    overlap = "pass" if user is None else "fail"
    
    context = {
        'overlap': overlap,
    }

    return JsonResponse(context)
