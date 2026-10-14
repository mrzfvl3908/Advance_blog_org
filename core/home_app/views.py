from django.views.generic import ListView
from blog_app.models import Post


class IndexView(ListView):
    model = Post
    template_name = 'home_app/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(
            status=True,
            published_date__isnull=False,
        ).select_related(
            'category',
            'author',
        ).order_by(
            '-published_date',
            '-created_date',
        )[:6]
