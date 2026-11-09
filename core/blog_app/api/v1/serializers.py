from rest_framework import serializers
from ...models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)

    class Meta:
        model = Post
        fields = ['id','author','category','title','content','status','image','published_date','snippet','relative_url']
        read_only_fields = ['content']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
