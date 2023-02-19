from django.db import models
from Product.models import Product,Variation

# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=50)
    Date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.cart_id




class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation=models.ManyToManyField(Variation,blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self) -> str:
        return self.product

    def sub_total(self):
        sub_total=self.product.price * self.quantity
        return sub_total

