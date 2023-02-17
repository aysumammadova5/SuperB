from django.contrib import admin
from .models import *

# admin.site.register([ProductCategories,Tags,Product,Discount,ProductVersion,ProductImages,Property,PropertyValues,ProductPropertyValues,Reviews])

admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Product_version)
admin.site.register(Image)
admin.site.register(Review)