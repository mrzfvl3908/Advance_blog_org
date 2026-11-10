from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from ...models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404

# function api fbv
"""@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == 'GET':
        post = Post.objects.filter(status=True)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)"""

# fbv
"""@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        post.delete()
        return Response('delete successfully', status=status.HTTP_204_NO_CONTENT)"""

# ApiView
"""class PostList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer

    def get(self, request):
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)"""

# ApiView
"""class PostDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer

    def get(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response('delete successfully', status=status.HTTP_204_NO_CONTENT)"""


#GenericApi
"""class PostList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)"""


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile) #=> برای گرفتن یوزر هستش و نیازی به انتخاب یوزر به صورت لیست منو نیست همونی که لاگین هس نمایش میده


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()