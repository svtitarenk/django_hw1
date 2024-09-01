from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_product_list_from_cache():
    # если кэш не включен, обращаемся к БД
    if not CACHE_ENABLED:
        return Product.objects.all()
    # если кэш включен, получаем данные из кэша
    key = 'product_list'
    # обращаемся к django для получения кэша
    products = cache.get(key)
    # если мы получили продукты, возвращаем продукты
    if products is not None:
        return products
    products = Product.objects.all()
    # если продукты мы не получили из кэша, мы их должны туда положить
    cache.set(key, products)
    return products
