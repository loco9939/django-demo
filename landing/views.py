from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from urllib3 import Retry
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        "weather_data": {"weather": "아주 맑음", "temperature": "17도"},
        "members": ["hooni", "janny", "jisu"],
    }
    return render(request, "index.html", context)


def detail(request, name):
    users = [
        {"name": "hooni", "email": "hooni@naver.com", "hobby": "running"},
        {"name": "mina", "email": "mina@naver.com", "hobby": "dance"},
        {"name": "yami", "email": "yami@naver.com", "hobby": "reading"},
        {"name": "cool", "email": "cool@naver.com", "hobby": "surfing"},
        {"name": "jack", "email": "jack@naver.com", "hobby": "golf"},
    ]
    result = ""
    a_user = None
    for user in users:
        if user["name"] == name:
            # result += f"<h1>{user['name']}</h1><h1>{user['email']}</h1><h1>{user['hobby']}</h1>"
            a_user = user
            break
    return render(request, "landing/users.html", a_user)


def 월보여주는함수(requset, 월):
    month_list = []
    try:
        for m in range(1, 13):
            month_list.append(f"{m}월")
        return HttpResponse(month_list[월 - 1])
    except:
        return HttpResponse("다시 입력해주세요")
