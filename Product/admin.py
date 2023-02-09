from django.contrib import admin
from .models import Product
# Register your models here.

class Categoryadmin(admin.ModelAdmin):


    prepopulated_fields={'slug':('product_name',)}
    list_display=('product_name','price','is_available')

admin.site.register(Product,Categoryadmin) 