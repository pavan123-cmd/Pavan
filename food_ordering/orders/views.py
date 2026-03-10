from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodItem, Order, OrderItem
from .forms import OrderForm

# Display menu
def menu(request):
    food_items = FoodItem.objects.filter(available=True).order_by('category')
    return render(request, 'orders/menu.html', {'food_items': food_items})

# Add item to cart
def add_to_cart(request, food_item_id):
    cart = request.session.get('cart', {})
    cart[food_item_id] = cart.get(food_item_id, 0) + 1
    request.session['cart'] = cart
    return redirect('menu')

# View cart
def view_cart(request):
    cart = request.session.get('cart', {})
    food_items = FoodItem.objects.filter(id__in=cart.keys())
    cart_items = [{'item': item, 'quantity': cart[str(item.id)]} for item in food_items]
    total_price = sum(item['item'].price * item['quantity'] for item in cart_items)
    return render(request, 'orders/cart.html', {'cart_items': cart_items, 'total_price': total_price})

# Place order
def place_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('menu')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            total_price = 0
            order.save()

            for food_item_id, quantity in cart.items():
                food_item = get_object_or_404(FoodItem, id=food_item_id)
                total_price += food_item.price * quantity
                OrderItem.objects.create(order=order, food_item=food_item, quantity=quantity)

            order.total_price = total_price
            order.save()
            request.session['cart'] = {}
            return redirect('menu')
    else:
        form = OrderForm()

    return render(request, 'orders/place_order.html', {'form': form})
