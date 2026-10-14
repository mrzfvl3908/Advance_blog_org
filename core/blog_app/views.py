from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Category, Post


class PublishedPostMixin:
    """فقط پست‌های منتشرشده را برمی‌گرداند."""

    def get_queryset(self):
        return (
            Post.objects.filter(
                status=True,
                published_date__isnull=False,
            )
            .select_related("category", "author")
            .order_by("-published_date", "-created_date")
        )


class PostList(PublishedPostMixin, ListView):
    model = Post
    template_name = "blog_app/post_list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        self.search_query = self.request.GET.get("q", "").strip()
        self.category = None

        category_id = self.kwargs.get("category_id")

        if category_id is not None:
            self.category = get_object_or_404(
                Category,
                pk=category_id,
            )
            queryset = queryset.filter(category=self.category)

        if self.search_query:
            queryset = queryset.filter(
                title__icontains=self.search_query,
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        context["search_query"] = self.search_query
        return context


class PostDetail(PublishedPostMixin, DetailView):
    model = Post
    template_name = "blog_app/post_detail.html"
    context_object_name = "post"
    slug_url_kwarg = "slug"
