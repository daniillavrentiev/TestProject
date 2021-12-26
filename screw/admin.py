from django.contrib import admin

from .models import Categories,\
                    SubCategory,\
                    ProductTypeList,\
                    Product,\
                    ProductRange


class ProductsInlines(admin.TabularInline):

    pass


class ProductAdmin(admin.ModelAdmin):

    pass
    # inlines = [
    #     ProductsInlines,
    # ]


admin.site.register(Categories)
admin.site.register(SubCategory)
admin.site.register(ProductTypeList)
admin.site.register(Product)
admin.site.register(ProductRange)




