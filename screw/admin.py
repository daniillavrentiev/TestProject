from django.contrib import admin

from .models import Category, Product, ProductRange


admin.site.register(Product)
admin.site.register(ProductRange)
admin.site.register(Category)



