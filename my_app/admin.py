from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Product)
# admin.site.register(ProductImage)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
 
    class Meta:
       model = Product
 
@admin.register(ProductImage)
class PostImageAdmin(admin.ModelAdmin):
    pass