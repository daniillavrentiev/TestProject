from django.urls import path

from rest_framework import routers
from .views import CategoriesListViewSet


router = routers.SimpleRouter()
router.register('categories', CategoriesListViewSet, basename='categories')
# router.register('products', ProductsViewSet,
#                 basename='products')


urlpatterns = []
urlpatterns += router.urls