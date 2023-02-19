from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from Product.models import Product
from Product.models import Variation
from .models import Cart, CartItem


# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    products = Product.objects.get(id=product_id)  # get the product
    product_variation = []
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]

            try:
                variation = Variation.objects.get(
                    Product=products, variation_catagory__iexact=key, variation_value__iexact=value)
                product_variation.append(variation)

            except:
                pass

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    is_cartitem_exits = CartItem.objects.filter(
        cart=cart, product=products).exists()

    if is_cartitem_exits:

        cart_item = CartItem.objects.filter(cart=cart, product=products)
        ex_car_list = []
        id = []

        for item in cart_item:
            existing_cartitems = item.variation.all()
            ex_car_list.append(list(existing_cartitems))
            id.append(item.id)

        if product_variation in ex_car_list:
            index = ex_car_list.index(product_variation)
            index_id = id[index]
            item = CartItem.objects.get(product=products, id=index_id)
            item.quantity += 1
            item.save()
        else:
            cart_item = CartItem.objects.create(
                product=products, cart=cart, quantity=1)

            if len(product_variation) > 0:
                item.variation.clear()
                item.variation.add(*product_variation)
            item.save()

    else:

        cart_item = CartItem.objects.create(
            product=products,
            quantity=1,
            cart=cart,
        )

        if len(product_variation) > 0:
            cart_item.variation.clear()
            cart_item.variation.add(*product_variation)
        cart_item.save()

    return redirect('cart')


def remove_cart_item(request, product_id,cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)  # get the product
    cart_item = CartItem.objects.get(cart=cart, product=product,id=cart_item_id)
    try:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass

    return redirect('cart')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)  # get the product
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity < 1:
        pass
    else:
        cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=0,):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price*cart_item.quantity)
            quantity += (cart_item.quantity)
    except:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,

    }
    return render(request, 'store/cart.html', context)
