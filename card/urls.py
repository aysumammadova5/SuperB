from django.urls import path
from .views import *

urlpatterns = [
    path('add_new_address/', AddresView.as_view(), name='add_new_address'),
     path('wishlist/', WishlistView.as_view(), name='wishlist'),
      path('shopping_cart/', BasketView.as_view(), name = "shopping_cart"),
]