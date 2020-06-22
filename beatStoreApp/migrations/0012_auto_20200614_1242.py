# Generated by Django 3.0.5 on 2020-06-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beatStoreApp', '0011_auto_20200614_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='btnColor',
            field=models.CharField(blank=True, choices=[('color1', 'greenColor'), ('color2', 'purpleColor'), ('color3', 'pinkColor')], default='greenColor', max_length=30, null=True),
        ),
    ]