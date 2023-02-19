from . import views
from django.urls import path


urlpatterns = [
    
    path("",views.store,name='store'),
    path('catagory/<slug:category_slug>/',views.store,name='Product_by_category'),
    path('catagory/<slug:category_slug>/<slug:slug>/',views.product_detail,name='Product_detail'),
    
    path('search/',views.search,name='search')
]
 