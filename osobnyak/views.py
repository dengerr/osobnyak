from django.shortcuts import render


def page_view(request, template_name='index'):
    return render(request, f'{template_name}.html', {
        'template_name': template_name,
    })
