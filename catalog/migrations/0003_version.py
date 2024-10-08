# Generated by Django 5.0.7 on 2024-08-13 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_remove_product_date_change_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("version_number", models.PositiveIntegerField(default=0)),
                (
                    "name",
                    models.CharField(
                        help_text="Введите версию продукта",
                        max_length=100,
                        verbose_name="версия",
                    ),
                ),
                (
                    "is_current",
                    models.BooleanField(default=False, verbose_name="активная версия"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберите продукт из списка",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="catalog.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
        ),
    ]
