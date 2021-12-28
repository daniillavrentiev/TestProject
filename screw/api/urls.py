from django.urls import path

from rest_framework import routers
from .views import CategoriesViewSet, ProductsViewSet, ProductRangeViewSet, CategoryProductListViewSet


router = routers.SimpleRouter()
router.register('categories', CategoriesViewSet, basename='categories')
router.register('products', ProductsViewSet,
                basename='products')
router.register('product', ProductRangeViewSet, basename='product')
router.register('category_products', CategoryProductListViewSet, basename='category_products')


urlpatterns = []
urlpatterns += router.urls