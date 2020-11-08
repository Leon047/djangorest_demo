from django.contrib import admin

from .models import Tags, Users, Company


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'languages', 'tags')
    list_filter = ('languages', 'tags')
    list_display_links = ('id', 'languages')

@admin.register(Users)
class Users(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'tags')
    list_filter = ('tags',)
    list_display_links = ('id', 'user_name', 'tags')

class CompanyInline(admin.TabularInline):
    model = Company

class AuthorAdmin(admin.ModelAdmin):
    inlines = [CompanyInline,]
