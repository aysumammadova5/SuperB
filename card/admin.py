from django.contrib import admin
from .models import *

admin.site.register(ShoppingCart)
admin.site.register(NewAddress)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(wishlist)
admin.site.register(basket_item)
admin.site.register(basket)

# @admin.register()
# class ResipeAdmin(admin.ModelAdmin):
#     list_filter: Sequence[Union[str, Type[ListFilter], Tuple[str, Type[ListFilter]]]]
        







