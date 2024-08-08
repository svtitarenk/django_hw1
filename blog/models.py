from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите заголовок блога",
    )
    slug = models.CharField(
        max_length=200,
        verbose_name='slug',
        help_text="Введите slug",
        null=True,
        blank=True
    )
    body = models.TextField(
        verbose_name='Содержимое блога',
        help_text='Введите текст блога',
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to="blog/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение статьи",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="Дата создания",
        help_text="Укажите дату создания записи",
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано?',
        help_text='Опубликовано True/False'
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество просмотров',
        help_text='Введите количество просмотров'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
