# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import Category, Tag, Article


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', ]
    prepopulated_fields = {'slug': ('name', )}


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    prepopulated_fields = {'slug': ('name', )}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
