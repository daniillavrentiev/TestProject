# Generated by Django 4.0 on 2021-12-26 14:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='screw.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название продукта')),
                ('slug', models.SlugField(verbose_name='Slug для продукта')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение для продукта')),
                ('description_1', models.CharField(max_length=255, verbose_name='Описание продукта')),
                ('description21', models.IntegerField(verbose_name='Описание продукта')),
                ('product_type_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screw.category', verbose_name='Тип продукта')),
            ],
            options={
                'verbose_name_plural': 'Продукт',
            },
        ),
        migrations.CreateModel(
            name='ProductRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение для товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена товара')),
                ('description_1', models.CharField(max_length=255, verbose_name='Описание товара')),
                ('description_2', models.IntegerField(verbose_name='Описание товара')),
                ('bit_size', models.CharField(choices=[('ph1', 'PH1'), ('ph2', 'PH2'), ('ph3', 'PH3'), ('pz', 'PZ')], max_length=255, verbose_name='Размер под биту')),
                ('in_stock', models.BooleanField(default=True, verbose_name='Наличие товара')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания товара')),
                ('main_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screw.product', verbose_name='Основной продукт')),
            ],
            options={
                'verbose_name_plural': 'Товар',
            },
        ),
    ]
