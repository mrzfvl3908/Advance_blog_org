from rest_framework import serializers
from ...models import Post, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'category', 'title', 'content', 'status', 'image', 'published_date', 'snippet',
                  'relative_url']
        read_only_fields = ['author']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = CategorySerializer(instance.category).data
        view = self.context.get('view')
        is_detail = view and view.kwargs.get('pk')

        if is_detail: #=> گرفتن تکی موارد در صفحه جزییات نمایش نمیده
            data.pop('snippet', None)
            data.pop('relative_url', None)
        else: #=>  گرفتن در لیست و موارد رو د صفحه لیست پست ها نمایش نمیده
            data.pop('content', None)
            data.pop('snippet', None)
            data.pop('image', None)

        return data
