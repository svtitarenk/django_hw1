# Generated by Django 4.2.2 on 2024-08-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["category", "name"],
                "permissions": [
                    ("can_change_is_published", "Can change is_published"),
                    ("can_change_description", "Can change description"),
                    ("can_change_category", "Can change category"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(
                default=False,
                help_text="Опубликовано True/False",
                verbose_name="Опубликовано?",
            ),
        ),
    ]
