# Generated by Django 3.0.5 on 2020-06-18 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beatStoreApp', '0019_auto_20200618_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
    ]
