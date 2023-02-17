from django.urls import path
from .views import ProductDetailView,ProductListView

urlpatterns = [
    # path('product_list/', product_list, name='productlist'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
   
]