from django.contrib import admin
from .models import Product,Variation
# Register your models here.

class Categoryadmin(admin.ModelAdmin):


    prepopulated_fields={'slug':('product_name',)}
    list_display=('product_name','price','is_available')

class VariationAdmin(admin.ModelAdmin):
    list_display=('Product','variation_catagory','variation_value','is_active')
    list_editable=('is_active',)
admin.site.register(Product,Categoryadmin) 
admin.site.register(Variation,VariationAdmin) 