from django.urls import path
from .views import WishlistAPI,BasketAPI
urlpatterns=[
path('wishlist/', WishlistAPI.as_view(), name = "wishlist"),
path('basket/',BasketAPI.as_view(),name="basket")
]