from django.db import models
from django.utils import timezone


class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')
    product_range = models.ForeignKey('ProductRange', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    slug = models.SlugField(verbose_name='Slug для продукта')
    image = models.ImageField(verbose_name='Изображение для продукта')
    description_1 = models.CharField(max_length=255, verbose_name='Описание продукта')
    description21 = models.IntegerField(verbose_name='Описание продукта')

    def __str__(self):
        return f'Товар из списка продуктов -- {self.name} --, |' \
               f' Тип продукта -- {self.category.name} --,' \


    class Meta:
        verbose_name_plural = 'Продукт'


class ProductRange(models.Model):

    SIZE_CHOICE = (
        ('ph1', 'PH1'),
        ('ph2', 'PH2'),
        ('ph3', 'PH3'),
        ('pz', 'PZ')
    )

    name = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField()
    image = models.ImageField(verbose_name='Изображение для товара')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена товара')
    description_1 = models.CharField(max_length=255, verbose_name='Описание товара')
    description_2 = models.IntegerField(verbose_name='Описание товара')
    bit_size = models.CharField(max_length=255, choices=SIZE_CHOICE, verbose_name='Размер под биту')
    in_stock = models.BooleanField(default=True, verbose_name='Наличие товара')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товар'



