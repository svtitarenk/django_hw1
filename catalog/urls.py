from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('catalog/', product_list, name='product_list'),
    path('catalog/<int:pk>/', product_detail, name='product_detail'),
    path('contacts/', contacts, name='contacts'),
]
