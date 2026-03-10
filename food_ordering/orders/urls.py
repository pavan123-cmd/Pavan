from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('add_to_cart/<int:food_item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('place_order/', views.place_order, name='place_order'),
]
