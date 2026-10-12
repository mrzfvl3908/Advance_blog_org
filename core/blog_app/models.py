from django.db import models
from accounts_app.models import User


class Category(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    model blog
    """
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-published_date']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
