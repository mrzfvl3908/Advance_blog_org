from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog_app.models import Post


class PostList(ListView):
    model = Post
    # queryset = Post.objects.filter(status=True)
    context_object_name = 'posts'
    paginate_by = 6
    # ordering = ['-published_date']


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

