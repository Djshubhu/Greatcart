from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage

# Create your views here.\\\

def store(request,category_slug=None):

     categories=None
     Products=None


     if category_slug != None:
          categories=         get_object_or_404(Category, slug = category_slug )
          Products=           Product.objects.filter(category=categories,is_available=True).order_by('id')
          paginator=Paginator(Products,2)
          page= request.GET.get('page')
          paged_products=paginator.get_page(page)
          Product_count=      Products.count()
     else:
          Products=           Product.objects.all().filter(is_available=True)
          paginator=Paginator(Products,3)
          page= request.GET.get('page')
          paged_products=paginator.get_page(page)
          Product_count=      Products.count()


     context = {
          'products': paged_products,
          'count': Product_count,
          categories:'Category'
     }
     return render(request,'store/store.html',context)


def product_detail(request,category_slug,slug):
     try:
          single_product=Product.objects.get(category__slug=category_slug,slug=slug)
          in_cart=CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
          
     except Exception as e:
          raise e     
     context={
          'singleProduct':single_product,
          'in_cart':in_cart
     }
     return render(request,'store/product_detail.html',context)

def search(request):
          if "keyword" in request.GET:
               keyword=request.GET['keyword']
               if keyword:
                    products=Product.objects.order_by("modiflied_date").filter(product_name__icontains=keyword)
                    Product_count=      products.count()
          context={
               'products' : products,
               'count':Product_count
          }
          return render(request,'store/store.html',context)