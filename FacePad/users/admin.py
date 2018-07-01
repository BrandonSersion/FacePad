from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Content, Rate, Comment, Friend

@admin.register(User)
class UserAdmin(UserAdmin):
    pass

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    pass

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass