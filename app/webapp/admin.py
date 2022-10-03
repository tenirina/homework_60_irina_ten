from django.contrib import admin

from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category', 'balance', 'price', 'created_at')
    list_filter = ('id', 'title', 'description', 'category')
    search_fields = ('title', 'description', 'category')
    fields = ('id', 'title', 'description', 'category', 'balance', 'price', 'created_at')
    readonly_fields = ('id', 'title', 'category')


admin.site.register(Product, ProductAdmin)
