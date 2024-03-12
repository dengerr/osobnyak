from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderingMixin(models.Model):
    ordering = models.SmallIntegerField(default=10)

    class Meta:
        abstract = True
        ordering = [
            'ordering',
        ]


class Category(OrderingMixin):
    class Page(models.IntegerChoices):
        HOUSES = 0, _('Дома, коттеджи')
        MODULES = 1, _('Модульные строения')

    page = models.SmallIntegerField(choices=Page.choices)
    title = models.CharField(max_length=127)
    slug = models.SlugField()

    class Meta:
        ordering = [
            'page',
            'ordering',
        ]

    def __str__(self):
        return f'{self.get_page_display()} - {self.title}'


class Product(OrderingMixin):
    title = models.CharField(max_length=127)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=31)
    description = models.TextField()
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            'category__page',
            'category__ordering',
            'ordering',
        ]


class ProductImage(OrderingMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products')
