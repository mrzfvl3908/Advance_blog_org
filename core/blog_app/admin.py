# from django.contrib import admin
# from blog_app.models import Post, Category
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'created_date']
#     search_fields = ['name']
#
#
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['author', 'title', 'published_date', 'status']
#     list_filter = ['status', 'created_date']
#     search_fields = ['title']
#
#
# admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)


from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_date',
        'updated_date',
    )

    readonly_fields = (
        'created_date',
        'updated_date',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'status',
        'created_date',
        'updated_date',
        'published_date',
    )

    list_filter = (
        'status',
        'category',
        'created_date',
        'published_date',
    )

    search_fields = (
        'title',
        'content',
    )

    readonly_fields = (
        'created_date',
        'updated_date',
    )

    prepopulated_fields = {
        'slug': ('title',),
    }
