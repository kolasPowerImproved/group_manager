# Generated by Django 2.0.2 on 2018-02-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20180212_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='groups',
            field=models.ManyToManyField(related_name='children', to='base.Group'),
        ),
    ]
