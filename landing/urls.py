from calendar import month
from django.urls import path
from . import views

app_name = "landing"
urlpatterns = [
    path("", views.index, name="home"),
    path("<int:월>/", views.월보여주는함수),
    # path("<str:name>/", views.detail),
]
