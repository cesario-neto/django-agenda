from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = 'name',
    ordering = '-id',
    list_per_page = 20
    list_max_show_all = 100


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'phone', 'category', 'show',
    ordering = '-id',
    list_filter = 'created_date', 'category',
    search_fields = 'first_name', 'last_name',
    list_editable = 'phone', 'category', 'show',
    list_per_page = 20
    list_max_show_all = 100
    list_display_links = 'first_name', 'last_name',
