# Generated by Django 2.0.2 on 2018-04-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_group_images_for_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesforslider',
            name='groups_image',
            field=models.ManyToManyField(related_name='images', to='base.Group'),
        ),
    ]
