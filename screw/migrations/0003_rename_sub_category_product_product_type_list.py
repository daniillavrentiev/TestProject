# Generated by Django 4.0 on 2021-12-24 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screw', '0002_alter_producttypelist_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sub_category',
            new_name='product_type_list',
        ),
    ]