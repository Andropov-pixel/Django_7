from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Эл.почта")
    avatars = models.ImageField(upload_to='users/avatars', blank=True, null=True, verbose_name='Аватар',
                              help_text='Загрузити фотографию')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', help_text='Введите номер телефона', blank=True, null=True)
    country = models.CharField(max_length=40, verbose_name="Страна", blank=True, null=True,
                               help_text="Введите страну проживания")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = "Пользователи"