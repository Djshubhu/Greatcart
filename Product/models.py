from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name      =   models.CharField(max_length=50)
    slug =                models.SlugField(max_length=50)
    description=          models.CharField(max_length=250)
    stock   =             models.IntegerField(default=10)
    price=                models.IntegerField()
    is_available=         models.BooleanField(default=True)
    images=               models.ImageField(upload_to='Photos/products')
    category=             models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date=         models.DateTimeField(auto_now_add=True)
    modiflied_date=       models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.product_name
    
    def get_url(self):
        return reverse('Product_detail',args=[self.category.slug,self.slug])