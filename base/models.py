from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Child(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    phone_regex = RegexValidator(regex=r'^\+38\(0\d{2}\)\ ?(?:\d(?:-|\.|\ )?){6}\d$',
                                 message="Номер телефону має бути введений в форматі: '+380999999'. Включає в себе 15 символім.")

    child_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    parents_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    gender = models.BooleanField(default=False)

    parents_name = models.CharField(max_length=100)

    date_of_birth = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('Дитина')
        verbose_name_plural = _('Діти')


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    group_description = models.CharField(max_length=500)
    group_image = models.FileField(upload_to='base/images/')
    group_music = models.FileField(upload_to='base/music/')

    class Meta:
        verbose_name = _('Група')
        verbose_name_plural = _('Групи')
