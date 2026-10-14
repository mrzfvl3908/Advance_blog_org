from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('post_list/', views.PostList.as_view(), name='post_list'),
    path('post_detail/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
]
