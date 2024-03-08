from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


def page_view(request, template_name='index'):
    if template_name == 'favicon.ico':
        return HttpResponse('')

    context = {
        'template_name': template_name,
    }

    if template_name == 'catalog':
        context['items'] = Product.objects.all().order_by(
            'category__ordering', 'ordering')

    return render(request, f'{template_name}.html', context)
