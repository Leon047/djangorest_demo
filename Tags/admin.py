from django.contrib import admin

from .models import Tags, Users


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','languages', 'tags')
    list_filter = ('languages', 'tags')

@admin.register(Users)
class Users(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'tags')
    list_filter = ('tags',)
