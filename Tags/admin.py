from django.contrib import admin

from .models import Tags, Users


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tags',)
    list_filter = ('id',)

@admin.register(Users)
class Users(admin.ModelAdmin):
    list_display = ('id', 'users')
