from django.shortcuts import render

# Create your views here.
# ---------------------------
# Vista del Store (almacen)
# ---------------------------
def store(request):
	context={}
	return render(request, 'store/store.html', context)
# ---------------------------
# Vista del Carrito (Cart)
# ---------------------------
def cart(request):
	context={}
	return render(request, 'store/cart.html', context)
# ---------------------------
# Vista de la compra 
# ---------------------------
def checkout(request):
	context={}
	return render(request, 'store/checkout.html', context)