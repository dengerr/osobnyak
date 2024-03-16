from django.shortcuts import render

from .models import Product, Category


def index_view(request):
    return render(request, f'index.html', {
        'template_name': 'index',
    })


def catalog_view(request):
    return render(request, f'catalog.html', {
        'template_name': 'catalog',
        'items': Product.objects.filter(
            category__page=Category.Page.MODULES,
            enabled=True,
        ).order_by(
            'category__ordering',
            'ordering',
        ),
    })


def houses_view(request):
    return render(request, f'houses.html', {
        'template_name': 'houses',
        'items': Product.objects.filter(
            category__page=Category.Page.HOUSES,
            enabled=True,
        ).order_by(
            'category__ordering',
            'ordering',
        ),
    })
