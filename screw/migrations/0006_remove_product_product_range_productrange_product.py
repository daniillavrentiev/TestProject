# Generated by Django 4.0 on 2021-12-27 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('screw', '0005_remove_productrange_main_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_range',
        ),
        migrations.AddField(
            model_name='productrange',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='screw.product', verbose_name='Основной продукт'),
            preserve_default=False,
        ),
    ]
