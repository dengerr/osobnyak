from django.contrib import admin

from .models import Category, Product, ProductImage


class ImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'title', 'slug', 'page', 'ordering'
    list_editable = 'ordering',


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'title', 'category', 'ordering', 'enabled'
    list_editable = 'ordering', 'enabled'
    inlines = [ImageInline]
