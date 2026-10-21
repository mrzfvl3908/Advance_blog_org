from django.db.models import Count, Q
from blog_app.models import Category, Post


def blog_sidebar(request):
    published_posts = Post.objects.filter(
        status=True,
        published_date__isnull=False,
    )

    return {
        'sidebar_recent_posts': published_posts.select_related(
            'category',
            'author',
        ).order_by(
            '-published_date',
            '-created_date',
        )[:5],

        'sidebar_categories': Category.objects.annotate(
            posts_count=Count(
                'posts',
                filter=Q(
                    posts__status=True,
                    posts__published_date__isnull=False,
                ),
            ),
        ).filter(
            posts_count__gt=0,
        ).order_by('name'),
    }
