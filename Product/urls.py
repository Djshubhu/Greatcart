from . import views
from django.urls import path


urlpatterns = [
    
    path("",views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='Product_by_category'),
    path('<slug:category_slug>/<slug:slug>/',views.product_detail,name='Product_detail')
]
 