from django.contrib import admin
from accounts_app.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email','full_name']

admin.site.register(User, UserAdmin)
