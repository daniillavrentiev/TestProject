from rest_framework import viewsets

from .serializers import ProductTypeListSerializer


from ..models import *


# class CategoriesListViewSet(viewsets.ModelViewSet):
#
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer
#
#     action_to_serializer = {
#         "list": ProductTypeListSerializer,
#         "retrieve": ProductTypeListSerializer
#     }
#
#     def get_serializer_class(self):
#         return self.action_to_serializer.get(
#             self.action,
#             self.serializer_class
#         )
#
#
# class ProductsViewSet(viewsets.ModelViewSet):
#
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     action_to_serializer = {
#         "list": ProductsSerializer,
#         "retrieve": ProductsSerializer
#     }
#
#     def get_serializer_class(self):
#         return self.action_to_serializer.get(
#             self.action,
#             self.serializer_class
#         )

class CategoriesListViewSet(viewsets.ModelViewSet):

    queryset = ProductTypeList.objects.all()
    serializer_class = ProductTypeListSerializer

