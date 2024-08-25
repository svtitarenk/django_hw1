from django.db import models
from django.utils.timezone import now

from users.models import User


# Create your models here.


# создаем модель категории как одного ко многим
class Category(models.Model):
    # наименование, описание
    name = models.CharField(
        max_length=100, verbose_name="категория", help_text="Введите категорию продукта"
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории продукта",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name} {self.description}"


# создаем модель продуктов как многих к одной категории. Ссылка на категорию
# создаем класс и наследуемся от models.Model
class Product(models.Model):
    # имя, порода, фото, дата рождения
    # создаем поля и прописываем их параметры
    name = models.CharField(
        max_length=100,
        verbose_name="наименование",
        help_text="введите наименование продукта",
    )
    description = models.TextField(
        max_length=100, verbose_name="описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="введите категорию продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.PositiveIntegerField(default=0, )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="дата создания",
        help_text="Укажите дату создания записи в БД",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="дата последнего изменения",
        help_text="Укажите дату изменения записи в БД",
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца продукта",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовано?',
        help_text='Опубликовано True/False'
    )

    # Класс мета
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        permissions = [
            ("can_change_is_published", "Can change is_published"),
            ("can_change_description", "Can change description"),
            ("can_change_category", "Can change category"),
        ]

    # строковое представление объекта
    def __str__(self):
        return f"{self.name} {self.category} {self.created_at}"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Продукт",
        help_text="Выберите продукт из списка",
    )
    version_number = models.PositiveIntegerField(
        default=0
    )
    name = models.CharField(
        max_length=100,
        verbose_name="версия",
        help_text="Введите версию продукта"
    )
    is_current = models.BooleanField(
        default=False,
        verbose_name="активная версия"
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

    def __str__(self):
        return f"{self.product.name} {self.version_number} {self.name}"
