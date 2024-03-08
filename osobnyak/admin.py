from django.contrib import admin

from .models import Category, Product, ProductImage


class ImageInline(admin.TabularInline):
    model = ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'title', 'slug', 'ordering'
    list_editable = 'ordering',


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'title', 'category', 'ordering'
    list_editable = 'ordering',
    inlines = [ImageInline]
