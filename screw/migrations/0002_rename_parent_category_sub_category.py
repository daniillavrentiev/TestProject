# Generated by Django 4.0 on 2021-12-27 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screw', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parent',
            new_name='sub_category',
        ),
    ]
