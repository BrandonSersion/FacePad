from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Content

@admin.register(User)
class UserAdmin(UserAdmin):
    pass


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    pass