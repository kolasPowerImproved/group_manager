# Generated by Django 2.0.2 on 2018-04-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20180416_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesforslider',
            name='image_name',
            field=models.CharField(default='Image', max_length=100, unique=True, verbose_name='Назва'),
        ),
    ]
