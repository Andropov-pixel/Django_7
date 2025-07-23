from django.db import models
from pygments.lexer import default

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='название', help_text='Введите название')
    content = models.TextField(verbose_name='содержимое', help_text='Введите содержимое')
    image = models.ImageField(upload_to='blog_image/', blank=True, null=True, verbose_name='фото',
                              help_text='Загрузити фотографию')
    created_at = models.DateField(verbose_name='дата создания', help_text='Введите датe создания', blank=True,
                                  null=True)
    publication_sign = models.BooleanField(default=True)
    count_of_views = models.PositiveIntegerField(verbose_name='Счетчик просмотров', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['title']