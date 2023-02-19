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


    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.product_name
    
    def get_url(self):
        return reverse('Product_detail',args=[self.category.slug,self.slug])




class VariationManager(models.Manager):
    def colours(self):
        return super(VariationManager,self).filter(variation_catagory='colour',is_active=True)
        
    def sizes(self):
        return super(VariationManager,self).filter(variation_catagory='size',is_active=True)

variation_catagory_choices=(
    ('colour','colour'),
    ('size','size'),
)



class Variation(models.Model):
    Product=             models.ForeignKey("Product", on_delete=models.CASCADE)
    variation_catagory = models.CharField(max_length=100,choices=variation_catagory_choices)
    variation_value    = models.CharField(max_length=100)
    is_active          = models.BooleanField(default=True)
    created_date       = models.DateTimeField(auto_now=True)

    
    
    objects=VariationManager()

    def __str__(self):
        return self.variation_value