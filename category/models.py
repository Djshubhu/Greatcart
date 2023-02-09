from django.db import models
from django.urls import reverse
from django.shortcuts import HttpResponse

# Create your models here.
class Category(models.Model):
    Category_name=       models.CharField(max_length=50 )
    slug =               models.SlugField(max_length=50 )
    description  =       models.TextField(max_length=50 ,blank=True)
    cat_img       =      models.ImageField(upload_to= 'Photos/images' , blank=True)
    is_available  =      models.BooleanField(default=True)


    class Meta:
        verbose_name        = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.Category_name

    def get_url(self):
        return reverse('Product_by_category',args=[self.slug])

    
    

            