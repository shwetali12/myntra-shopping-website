from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
   path('',views.index,name='index'),

   path('men/',views.men, name='men'),
   path('women/', views.women,name='women'),
   path('wishlist/',views.wishlist,name='wishlist'),

   path('kids/',views.kids,name='kids'),
   path('login/',views.user_login,name='login'),
   path('signup/',views.signup,name='signup'),
   path('logout/',views.logoutpage,name='logout'),
   path('details/<int:id>/', views.details, name='details'),
   path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
   path('add_to_cart_from_wishlist/<int:id>/', views.add_to_cart_from_wishlist, name='add_to_cart_from_wishlist'),
   path('search/', views.product_search, name='product_search'),
   path('add_to_wishlist/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),
   path('place_order/<int:id>/',views.place_order,name='place_order'),

   path('cart/', views.cart, name='cart'),
   path('remove_from_cart/<int:id>/',views.remove_from_cart,name='remove_from_cart'),
   path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
   path('order/',views.order,name='order'),
  

]