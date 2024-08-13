from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, ProductList, ProductDetailView, ContactsView, ProductCreate, ProductDeleteView, \
    ProductUpdate

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductList.as_view(), name='home'),
    path('home/', ProductList.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', ProductList.as_view(), name='product_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/create/', ProductCreate.as_view(), name='product_create'),
    path('catalog/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
]


