from django.contrib import admin

from products.models import ProductCategory, Product, Basket


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', 'description', 'price', 'quantity', 'category', 'image')
    search_fields = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0