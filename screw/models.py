from django.db import models
from django.utils import timezone


class Categories(models.Model):

    name = models.CharField(verbose_name='Название Основной Категории', max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Название категории {self.name}'

    class Meta:
        verbose_name_plural = 'Категория Продукта'


class SubCategory(models.Model):

    category = models.ForeignKey(Categories, verbose_name='Основная Категория', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название ПодКатегории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'Название ПодКатегории {self.name} | ' \
               f'Название Основной Категории {self.category.name}'

    class Meta:
        verbose_name_plural = 'ПодКатегория Продукта'


class ProductTypeList(models.Model):

    sub_category = models.ForeignKey(SubCategory, verbose_name='ПодКатегория Продукта', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Тип Продукта')
    slug = models.SlugField()

    def __str__(self):
        return f'Название типа продукта {self.name} | ' \
               f'Название  ПодКатегории продукта {self.sub_category.name}'

    class Meta:
        verbose_name_plural = 'Тип продукта Продукта ПодКатегории'


class Product(models.Model):

    product_type_list = models.ForeignKey(ProductTypeList, verbose_name='Тип продукта', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    slug = models.SlugField(verbose_name='Slug для продукта')
    image = models.ImageField(verbose_name='Изображение для продукта')
    description_1 = models.CharField(max_length=255, verbose_name='Описание продукта')
    description21 = models.IntegerField(verbose_name='Описание продукта')

    def __str__(self):
        return f'Товар из списка продуктов -- {self.name} --, |' \
               f' Тип продукта -- {self.product_type_list.name} --,' \
               f' | ПодКатегория продукта -- {self.product_type_list.sub_category.name} --'

    class Meta:
        verbose_name_plural = 'Продукт'


class ProductRange(models.Model):

    SIZE_CHOICE = (
        ('ph1', 'PH1'),
        ('ph2', 'PH2'),
        ('ph3', 'PH3'),
        ('pz', 'PZ')
    )

    main_product = models.ForeignKey(Product, verbose_name='Основной продукт', on_delete=models.CASCADE)
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
        return f'Товар  -- {self.name} --, | который относиться к продукту -- {self.main_product.name} -- ' \
               f'| Назвние типа продукта -- {self.main_product.product_type_list.name} --'

    class Meta:
        verbose_name_plural = 'Товар'



