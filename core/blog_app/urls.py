from django.urls import path

from . import views

app_name = 'blog_app'

urlpatterns = [
    path(
        'post_list/',
        views.PostList.as_view(),
        name='post_list',
    ),
    path(
        'posts/category/<int:category_id>/',
        views.PostList.as_view(),
        name='category_posts',
    ),
    path(
        'post_detail/<slug:slug>/',
        views.PostDetail.as_view(),
        name='post_detail',
    ),
    path('create/post/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
