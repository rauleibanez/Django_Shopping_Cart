from django.shortcuts import render
from .models import *

# Create your views here.
# ---------------------------
# Vista del Store (almacen)
# ---------------------------
def store(request):
	products = Product.objects.all()
	context={'products':products}
	return render(request, 'store/store.html', context)
# ---------------------------
# Vista del Carrito (Cart)
# ---------------------------
def cart(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items =[]
		order ={'get_cart_total':0, 'get_cart_items':0}
	context={'items':items, 'order':order}
	return render(request, 'store/cart.html', context)
# ---------------------------
# Vista de la compra 
# ---------------------------
def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		# Crea un carro vacio para los usuarios no loggeados
		items =[]
		order ={'get_cart_total':0, 'get_cart_items':0}
	context={'items':items, 'order':order}
	return render(request, 'store/checkout.html', context)