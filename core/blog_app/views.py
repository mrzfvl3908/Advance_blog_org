from django.shortcuts import render
from django.views.generic import ListView
from blog_app.models import Post


class PostList(ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)[:6]
    context_object_name = 'posts'
