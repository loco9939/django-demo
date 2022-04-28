from django.urls import path
from . import views

app_name = "blog"
# blog/ 경로를 작성해주는 곳
urlpatterns = [
    path("", views.index),
    path("home/", views.blog_home, name="home"),
    path("post-write/", views.blog_post_write, name="create"),
    path("post-view/<int:post_id>/", views.blog_post_view, name="detail"),
    path("post-edit/<int:post_id>/", views.blog_post_update, name="edit"),
    path("post-delete/<int:post_id>/", views.blog_post_delete),
]
