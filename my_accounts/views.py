from audioop import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def sign_up(request):
    if request.user.is_authenticated:
        return redirect("blog:home")
    # 요청이 post인지 확인

    context = {}
    if request.method == "POST":

        # 1. 요청받은 request에서 username 존재하는지?
        # 2. 요청받은 request에서 password 존재하는지?
        # 3. 요청받은 request에서 password == password_check 참인지?
        # get 써준 이유는 없을 경우 기본값을 넣어줘서 오류 발생시키지 않게 하려고
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_check = request.POST.get("password_check")
        if username and password and password == password_check:
            try:
                new_user = User.objects.create_user(
                    username=username, password=password
                )
                auth.login(request, new_user)
                print("로그인 성공!")
                return redirect("blog_samples:home")
            except:
                context["error"] = "이미 존재하는 아이디입니다."
        else:
            context["error"] = "아이디 또는 비밀번호를 잘못 입력하셨습니다."

        # 회원가입 ok
        # 새로운 유저 아이디 로그인
        # 블로그 홈으로 리다이렉트 시켜주기

    # 에러메시지 context에 담기
    return render(request, "my_accounts/sign_up.html", context)


def login(request):
    context = {}
    # 요총이 post인지 확인
    if request.method == "POST":

        # 1. 아이디 확인
        # 2. 비밀번호 확인
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = auth.authenticate(request, username=username, password=password)

            if user:
                auth.login(request, user)
                return redirect("blog_samples:home")
            else:
                context["error"] = "아이디랑 비밀번호 틀렸습니다."
        else:
            context["error"] = "아이디 혹은 비밀번호를 입력해주세요..."
        # 비밀번호 체크
        # 로그인0
        # 리다이렉트
        print(context["error"])
    return render(request, "my_accounts/login.html", context)

def logout(request):
    # 요청이 post 인지 확인
    # if request.method == "POST":
    auth.logout(request)
        # 로그아웃 o
        
    #redirect
    return redirect('blog_samples:home')

def naver_test(request):
    return render(request,'my_accounts/naver_test.html')
