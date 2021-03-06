# Generated by Django 2.0.2 on 2018-02-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='trainer_phone_number',
            field=models.CharField(blank=True, max_length=17, verbose_name='Номер телефону'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_image',
            field=models.FileField(upload_to='base/static/images/', verbose_name='Зображення'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_music',
            field=models.FileField(upload_to='base/static/music/', verbose_name='Музика'),
        ),
    ]
