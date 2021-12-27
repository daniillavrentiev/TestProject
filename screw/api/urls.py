from django.urls import path

from rest_framework import routers
from .views import CategoriesViewSet, ProductsViewSet


router = routers.SimpleRouter()
router.register('categories', CategoriesViewSet, basename='categories')
router.register('products', ProductsViewSet,
                basename='products')


urlpatterns = []
urlpatterns += router.urls