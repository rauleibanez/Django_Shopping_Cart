from django.urls import path
from . import views
# ----------------------------
# URLS de las vistas de la App 
# Store
# ----------------------------
urlpatterns = [
	path('', views.store, name='store'),
	path('cart/', views.cart, name='cart'),
	path('checkout/', views.checkout, name='checkout'),
] 
