from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='название', help_text='Введите название')
    description = models.TextField(max_length=250, verbose_name='описание', help_text='Введите описание')
    image = models.ImageField(upload_to='product/photo', blank=True, null=True, verbose_name='фото',
                              help_text='Загрузити фотографию')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='категория',
                                 help_text='Введите категорию', blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена', help_text='Введите цену', blank=True, null=True)
    created_at = models.DateField(verbose_name='дата создания', help_text='Введите датe создания', blank=True,
                                  null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения', blank=True, null=True)
    is_available = models.BooleanField(default=False, verbose_name="Доступность в каталоге")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        related_name="products",
        null=True,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("remove_any_product", "Remove any product"),
        ]


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='название', help_text='Введите название', blank=True,
                            null=True)
    description = models.TextField(max_length=250, verbose_name='описание', help_text='Введите описание', blank=True,
                                   null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'