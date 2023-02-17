from django.urls import path
from blog.api.views import blogs


urlpatterns = [ 
    path('blogs/', blogs, name= 'blogs'),
    path('blogs/<int:pk>/', blogs, name= 'blogs')

]