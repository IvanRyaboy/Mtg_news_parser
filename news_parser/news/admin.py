from django.contrib import admin
from .models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(MagicNews)
class MagicNewsAdmin(admin.ModelAdmin):
    list_display = ['title',]


@admin.register(NewsType)
class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ['type',]
