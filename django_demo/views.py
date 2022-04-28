from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "로딩 성공 했어요"
    )
