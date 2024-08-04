from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, ProductList, ProductDetailView, ContactsView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductList.as_view(), name='home'),
    path('home/', ProductList.as_view(), name='home'),
    path('catalog/', ProductList.as_view(), name='product_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
]
