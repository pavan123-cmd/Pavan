from django.contrib import admin
from .models import FoodItem, Order, OrderItem

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')
    fields = ('name', 'description', 'price', 'category', 'available', 'image')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'date_ordered', 'total_price')
    inlines = []

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'food_item', 'quantity')
