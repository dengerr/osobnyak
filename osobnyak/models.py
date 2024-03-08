from django.db import models


class OrderingMixin(models.Model):
    ordering = models.SmallIntegerField(default=10)

    class Meta:
        abstract = True
        ordering = [
            'ordering',
        ]


class Category(OrderingMixin):
    title = models.CharField(max_length=127)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Product(OrderingMixin):
    title = models.CharField(max_length=127)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=31)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            'category__ordering',
            'ordering',
        ]


class ProductImage(OrderingMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products')
