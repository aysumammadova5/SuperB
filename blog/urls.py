from django.urls import path
from .views import *


urlpatterns = [
    path('blog_list/', BlogView.as_view(), name='blogs'),
    path('blog_detail/<slug:slug>', BlogDetailView.as_view(), name='blog_detail'),
]