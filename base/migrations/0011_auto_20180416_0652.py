# Generated by Django 2.0.2 on 2018-04-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_imagesforslider_groups_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagesforslider',
            name='groups_image',
        ),
        migrations.AddField(
            model_name='group',
            name='images_for_slider',
            field=models.ManyToManyField(related_name='images', to='base.Group'),
        ),
    ]
