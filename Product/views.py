from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.\\\

def store(request,category_slug=None):

     categories=None
     Products=None


     if category_slug != None:
          categories=         get_object_or_404(Category, slug = category_slug )
          Products=           Product.objects.filter(category=categories,is_available=True)
          Product_count=      Products.count()
     else:
          Products=           Product.objects.all().filter(is_available=True)
          Product_count=      Products.count()


     context = {
          'products': Products,
          'count': Product_count,
          categories:'Category'
     }
     return render(request,'store/store.html',context)


def product_detail(request,category_slug,slug):
     try:
          single_product=Product.objects.get(category__slug=category_slug,slug=slug)
     except Exception as e:
          raise e     
     context={
          'singleProduct':single_product
     }
     return render(request,'store/product_detail.html',context)