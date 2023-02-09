from django.shortcuts import render
from Product.models import Product

def home(request):
    Products = Product.objects.all().filter(is_available=True)
    context={
        'products':Products
    }
    return render(request,'home.html',context)


