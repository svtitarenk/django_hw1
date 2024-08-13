from django.contrib import admin
from catalog.models import Product, Category, Version


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description",)
    list_filter = ("name",)
    search_fields = ("name", "description",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "created_at",)
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("product", "version_number", "name", "is_current",)
    list_filter = ("product",)
    search_fields = ("version_number", "name",)
