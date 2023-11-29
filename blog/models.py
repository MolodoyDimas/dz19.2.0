from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, null=True, verbose_name='slug')
    body = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='image/', verbose_name='Изображение', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    pudlished = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
        ordering = ('title',)