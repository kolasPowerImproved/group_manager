# Generated by Django 2.0.2 on 2018-02-08 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name="Ім'я")),
                ('second_name', models.CharField(max_length=50, verbose_name='По батькові')),
                ('last_name', models.CharField(max_length=50, verbose_name='Прізвище')),
                ('date_of_birth', models.DateField(verbose_name='Дата народження')),
                ('child_phone_number', models.CharField(blank=True, max_length=17, verbose_name='Номер телефону дитини')),
                ('parents_phone_number', models.CharField(blank=True, max_length=17, verbose_name='Номер телефону батьків')),
                ('gender', models.CharField(choices=[('M', 'Хлопець'), ('F', 'Дівчина')], default='M', max_length=1)),
                ('parents_name', models.CharField(max_length=100, verbose_name="Ім'я батьків")),
                ('payment', models.IntegerField(default=250, verbose_name='Оплата')),
                ('date_of_payment', models.DateField(default='', verbose_name='Дата оплати')),
            ],
            options={
                'verbose_name': 'Дитина',
                'verbose_name_plural': 'Діти',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100, verbose_name='Назва')),
                ('group_description', models.CharField(max_length=500, verbose_name='Опис')),
                ('group_image', models.FileField(upload_to='base/images/', verbose_name='Зображення')),
                ('group_music', models.FileField(upload_to='base/music/', verbose_name='Музика')),
                ('salary', models.FloatField(default=0.3, max_length=10, verbose_name='Зарплата')),
            ],
            options={
                'verbose_name': 'Група',
                'verbose_name_plural': 'Групи',
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name="Ім'я")),
                ('second_name', models.CharField(max_length=100, verbose_name='По батькові')),
                ('last_name', models.CharField(max_length=100, verbose_name='Прізвище')),
            ],
            options={
                'verbose_name': 'Тренер',
                'verbose_name_plural': 'Тренери',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Trainer'),
        ),
        migrations.AddField(
            model_name='child',
            name='groups',
            field=models.ManyToManyField(to='base.Group'),
        ),
    ]
