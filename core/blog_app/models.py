# from django.db import models
# from django.urls import reverse
# from django.utils.text import slugify
#
# from accounts_app.models import User
# from django.contrib.auth import get_user_model
#
#
# # getting user model
# # User = get_user_model() => برای فراخوانی یوزر  از درون مدل اکانت
#
#
# class Category(models.Model):
#     """
#     this is  a class to define categories for posts in blog app
#     """
#     name = models.CharField(max_length=200)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name_plural = 'Categories'
#         verbose_name = 'Category'
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.name
#
#
# class Post(models.Model):
#     """
#     this is  a class to define posts for blog app
#     """
#     category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='posts')
#     author = models.ForeignKey('accounts_app.Profile', on_delete=models.SET_NULL, null=True, related_name='posts')
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     image = models.ImageField(upload_to='posts/', blank=True, null=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     slug = models.SlugField(unique=True, allow_unicode=True, blank=True)
#     status = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['-created_date']
#         verbose_name = 'Post'
#         verbose_name_plural = 'Posts'
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             base_slug = slugify(self.title, allow_unicode=True)
#             slug = base_slug
#             counter = 1
#
#             while self.__class__.objects.filter(slug=slug).exists():
#                 slug = f'{base_slug}-{counter}'
#                 counter += 1
#
#             self.slug = slug
#
#         super().save(*args, **kwargs)
#
#     # def get_absolute_url(self):
#     #     return reverse('blog_app:post-detail', kwargs={'slug': self.slug})
#
#     def __str__(self):
#         return self.title


from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='posts',
    )

    author = models.ForeignKey(
        'accounts_app.Profile',
        on_delete=models.CASCADE,
        related_name='posts',
    )

    title = models.CharField(max_length=200)
    content = models.TextField()

    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
    )

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    published_date = models.DateTimeField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        allow_unicode=True,
        blank=True,
    )

    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(
                self.title,
                allow_unicode=True,
            )

            # جلوگیری از اسلاگ خالی
            base_slug = base_slug or 'post'

            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def publish(self):
        self.status = True
        if self.published_date is None:
            self.published_date = timezone.now()

        self.save(update_fields=[
            'status',
            'published_date',
            'updated_date',
        ])

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse(
    #         'blog_app:post-detail',
    #         kwargs={'slug': self.slug},
    #     )
