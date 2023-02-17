from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from product.models import Product, Product_version
from .serializers import (
                    ProductReadSerializer, 
                    ProductVersionSerializer
                )
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from verify_email import verify_email
from django.contrib.auth.decorators import login_required


class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer

class ProductVersionAPI(ListAPIView):
    queryset = Product_version.objects.all()
    serializer_class = ProductVersionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product__category', 'color__name', 'product__manufacturer__name', 'product__category__p_category']
