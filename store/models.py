from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# ----------------------------------
# Clases de Modelos Complementarios
# ----------------------------------
# Clase de Clientes (Customer)
# ----------------------------------
class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=200, null=True)
	email= models.CharField(max_length=200)

	def __str__(self):
		return self.name
# ----------------------------------
# Clase de Productos (Product)
# ----------------------------------
class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	digital = models.BooleanField(default=False, null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	# ----------------------------
	# Funcion para corregir el
	# error cuando no hay imagen
	# en el producto
	# ----------------------------
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
# ----------------------------------
# Clase de Ordenes (Order)
# ----------------------------------
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
	# ------------------------------
	# funcion para el formulario de
	# Shipping 
	# ------------------------------
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping	
	# ------------------------------
	# funcion para obtener el total 
	# del carrito
	# ------------------------------	
	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total
	# ------------------------------
	# funcion para obtener los 
	# elementos del carrito
	# ------------------------------	
	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total	
# ----------------------------------
# Clase de Detalle de Ordenes 
# (OrderItem)
# ----------------------------------
class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	# ----------------------------
	# Funcion para totalizar 
	# pedidos
	# ----------------------------
	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
# ----------------------------------
# Clase de Direccion de Facturación 
# Cobro (ShippingAddress)
# ----------------------------------
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return (self.address)