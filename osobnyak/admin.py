from django.contrib import admin
from django.template import Template, Context

from .models import Category, Product, ProductImage


class ImageInline(admin.TabularInline):
    fields = 'ordering', 'miniature', 'image',
    readonly_fields = 'miniature',
    model = ProductImage

    def miniature(self, obj):
        template = Template('''{% load thumbnail %}
        <img src="{{ obj.image|thumbnail_url:'small' }}" alt="">''')
        return template.render(Context({'obj': obj}))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'title', 'slug', 'page', 'ordering'
    list_editable = 'ordering',


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'title', 'category', 'ordering', 'enabled'
    list_editable = 'ordering', 'enabled'
    inlines = [ImageInline]
