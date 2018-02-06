# Generated by Django 2.0.2 on 2018-02-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='payment',
            field=models.IntegerField(default=250, verbose_name='Оплата'),
        ),
        migrations.AlterField(
            model_name='group',
            name='salary',
            field=models.FloatField(default=0.3, max_length=10, verbose_name='Зарплата'),
        ),
    ]
