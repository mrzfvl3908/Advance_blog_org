from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
   path('post_list/', views.PostList.as_view(), name='post_list'),
]