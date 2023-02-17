from django.db import models
from product.models import Product,Product_version
# from core.models import TimeStamp
from django.contrib.auth import get_user_model
User=get_user_model()

class ShoppingCart(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.FloatField()
    # user_id = models.ForeignKey(Customer,on_delete = models.CASCADE)

class Country(models.Model):
    name = models.CharField(max_length=225)

class State(models.Model):
    name = models.CharField(max_length=225)

class NewAddress(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    telephone = models.IntegerField()
    street_address = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10)


class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_wishlist")
    product = models.ManyToManyField(Product_version, related_name="products_wishlist")

    def __str__(self):
        return f"{self.user}'s wishlist"

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists" 


class basket_item(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Product_version, on_delete=models.CASCADE, null=True, blank=True, related_name="product_basket_item")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_basket_item")

    def __str__(self):
        return f"{self.user.username}'s basket item"

    def get_subtotal(self):
        if self.product.product.in_sale:
            subtotal = self.product.product.new_price*self.quantity
        else:
            subtotal = self.product.product.price*self.quantity
        return subtotal

    class Meta:
        verbose_name = "Basket Item"
        verbose_name_plural = "Basket Items"

class basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_basket")
    items = models.ManyToManyField(basket_item, related_name="basket_items")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s basket"

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"







