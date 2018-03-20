from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Child(models.Model):
    """
    Description of the child class. Child can be in many groups and have many trainers
    At the moment phone number regex does not work
    """
    first_name = models.CharField(max_length=50, verbose_name='Ім\'я')                 # child's first name
    second_name = models.CharField(max_length=50, verbose_name='По батькові')          # child's parent's name
    last_name = models.CharField(max_length=50, verbose_name='Прізвище')               # child's last name

    date_of_birth = models.DateField(auto_now=False, auto_now_add=False,               # child's date of birth
                                     verbose_name='Дата народження')

    phone_regex = RegexValidator(regex=r'^\+38\(0\d{2}\)\ ?(?:\d(?:-|\.|\ )?){6}\d$',
                                 message="Номер телефону має бути введений в форматі: '+380999999'.")  #regex for phone number detect

    child_phone_number = models.CharField(max_length=17, blank=True,                   # child's phone number, using regex for detecting
                                          verbose_name='Номер телефону дитини')        # validators should be a list | validators=[phone_regex],
    parents_phone_number = models.CharField(max_length=17, blank=True,                 # parent's phone number, using regex for detecting
                                            verbose_name='Номер телефону батьків')
    groups = models.ManyToManyField('Group', related_name='children')

    #gender = models.BooleanField(default=False, verbose_name='Хлопець')                # if set false that's mean that a child is female,
                                                                                        # if set true, means that the child is male gender

    GENDER = (
        ("M", "Хлопець"),
        ("F", "Дівчина"),
    )
    gender = models.CharField(max_length=1, choices=GENDER, default='F')

    parents_name = models.CharField(max_length=100, verbose_name='Ім\'я батьків')         # parent's name

    payment = models.IntegerField(verbose_name='Оплата', default=250)                     # how many monet a child must to pay
    date_of_payment = models.DateField(auto_now=False, auto_now_add=False, default='',    # date of last payment
                                       verbose_name='Дата оплати')

    class Meta:
        verbose_name = _('Дитина')
        verbose_name_plural = _('Діти')

    def __str__(self):
        return self.last_name

    def full_name(self):
        full_name = '%s %s %s', self.last_name, self.first_name, self.second_name
        return full_name


class Group(models.Model):
    """
    Description of the group's class,
    one group can have many children and many trainers
    """
    group_name = models.CharField(max_length=100, verbose_name='Назва', unique=True)                    # group's name
    group_description = models.CharField(max_length=500, verbose_name='Опис')                           # short description of the group
    group_image = models.ImageField(upload_to='base/static/images/', verbose_name='Зображення')         # group's poster
    group_music = models.FileField(upload_to='base/static/music/', verbose_name='Музика')               # group's music. Can be many different music

    salary = models.FloatField(max_length=10, verbose_name='Зарплата', default=0.3)                     # salary per one child in the group
    trainer = models.ForeignKey('Trainer', models.CASCADE, null=True, blank=True)
    # addiction = models.ForeignKey('Child', on_delete=models.CASCADE)                                  # addiction with group and child

    monday_time = models.CharField(max_length=100, verbose_name='Понеділок', unique=False, default='-')
    tuesday_time = models.CharField(max_length=100, verbose_name='Вівторок', unique=False, default='-')
    wednesday_time = models.CharField(max_length=100, verbose_name='Середа', unique=False, default='-')
    thursday_time = models.CharField(max_length=100, verbose_name='Четвер', unique=False, default='-')
    friday_time = models.CharField(max_length=100, verbose_name="П'ятниця", unique=False, default='-')
    saturday_time = models.CharField(max_length=100, verbose_name='Субота', unique=False, default='-')
    sunday_time = models.CharField(max_length=100, verbose_name='Неділя', unique=False, default='-')

    images_for_slider = models.ManyToManyField('ImagesForSlider', related_name='children')

    class Meta:
        verbose_name = _('Група')
        verbose_name_plural = _('Групи')

    def __str__(self):
        return self.group_name

    def get_img(self):
        return self.group_image.url

    def get_image_gor_slider(self):
        return self.images_for_slider.url

    def music_name(self):
        return self.group_music


class Trainer(models.Model):
    """
    Describes trainer's class,
    can have many groups
    """
    first_name = models.CharField(max_length=100, verbose_name='Ім\'я')            # trainer's first name
    second_name = models.CharField(max_length=100, verbose_name='По батькові')     # trainer's parent's name
    last_name = models.CharField(max_length=100, verbose_name='Прізвище')          # trainer's last name

    phone_regex = RegexValidator(regex=r'^\+38\(0\d{2}\)\ ?(?:\d(?:-|\.|\ )?){6}\d$',
                                 message="Номер телефону має бути введений в форматі: '+380999999'.")  # regex for phone number detecting

    trainer_phone_number = models.CharField(max_length=17, blank=True, verbose_name='Номер телефону')  # validators should be a list | validators=[phone_regex],
    # here have a admin runtime error.
    # addiction = models.ForeignKey('Group', on_delete=models.CASCADE)               # addiction with trainer's and groups

    class Meta:
        verbose_name = _('Тренер')
        verbose_name_plural = _('Тренери')

    def __str__(self):
        return self.last_name


class ImagesForSlider(models.Model):
    image = models.ImageField(upload_to='base/static/images/')