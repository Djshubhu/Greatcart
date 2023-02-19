from django.contrib import admin
from .models import CartItem,Cart
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display=('cart_id','Date_added')

class CartItemsAdmin(admin.ModelAdmin):
    list_display=('product','cart','quantity','is_active')


admin.site.register(CartItem,CartItemsAdmin)
admin.site.register(Cart,CartAdmin)