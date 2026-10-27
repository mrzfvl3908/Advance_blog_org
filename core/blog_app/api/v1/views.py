from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from ...models import Post
from .serializers import PostSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view()
def postList(request):
    post = Post.objects.filter(status=True)
    serializer = PostSerializer(post, many=True)
    return Response(serializer.data)


@api_view()
def postDetail(request,id):
    post = get_object_or_404(Post, pk=id, status=True)
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)