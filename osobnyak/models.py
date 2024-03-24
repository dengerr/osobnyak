from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderingMixin(models.Model):
    ordering = models.SmallIntegerField(default=10, verbose_name='порядок')

    class Meta:
        abstract = True
        ordering = [
            'ordering',
        ]


class Category(OrderingMixin):
    class Page(models.IntegerChoices):
        HOUSES = 0, _('Дома, коттеджи')
        MODULES = 1, _('Модульные строения')

    page = models.SmallIntegerField(choices=Page.choices, verbose_name='страница')
    title = models.CharField(max_length=127, verbose_name='название')
    slug = models.SlugField()

    class Meta:
        ordering = [
            'page',
            'ordering',
        ]
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return f'{self.get_page_display()} - {self.title}'


class Product(OrderingMixin):
    title = models.CharField(max_length=127, verbose_name='название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.CharField(max_length=31, verbose_name='цена')
    description = models.TextField(verbose_name='описание')
    enabled = models.BooleanField(default=True, verbose_name='включено')

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            'category__page',
            'category__ordering',
            'ordering',
        ]
        verbose_name = "продукт"
        verbose_name_plural = "продукты"


class ProductImage(OrderingMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='продукт')
    image = models.ImageField(upload_to='products', verbose_name='картинка')

    class Meta:
        verbose_name = "картинка продукта"
        verbose_name_plural = "картинки продуктов"
