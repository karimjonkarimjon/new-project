from django.urls import path
from .views import cart, add_cart, sub_cart

urlpatterns = [
    path("cart/", cart, name="cart"),
    path('add_product/<int:product_id>/', add_cart, name="cart_add"),
    path('sub_product/<int:product_id>/', sub_cart, name="cart_sub"),
]
