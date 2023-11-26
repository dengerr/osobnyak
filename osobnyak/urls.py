from django.urls import path

from . import views

urlpatterns = [
    path('', views.page_view),
    path('<str:template_name>', views.page_view),
]
