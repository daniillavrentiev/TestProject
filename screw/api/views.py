from rest_framework import viewsets, response

from .serializers import CategorySerializer, ProductsSerializer

from ..models import *


class CategoriesViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @staticmethod
    def flat_tree(data):
        for key, value in data.items():
            if data.get(value['parent']):
                data[value['parent']]['sub_category'].append(value)
        return filter(lambda x: x['parent'] is None, data.values())

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        flat_tree_ = {c['id']: {'id': c['id'], 'name': c['name'], 'sub_category': [], 'parent': c['parent']}
                     for c in serializer.data}
        return response.Response(self.flat_tree(flat_tree_))


class ProductsViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

