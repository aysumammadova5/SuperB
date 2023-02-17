from django.shortcuts import render
from django.views.generic import CreateView
from .models import *
from .forms import *
from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class AddresView(CreateView):
    form_class = NewAddressForm
    template_name = 'contact_information.html'
   
    success_url = '/card/add_new_address'


class WishlistView(LoginRequiredMixin, ListView):
    model = wishlist
    template_name = 'wishlist.html'
    context_object_name = 'items'

    def get_queryset(self):
        user_wishlist =  wishlist.objects.filter(user = self.request.user).first()
        if user_wishlist:
            all_products = user_wishlist.product.all()
        return all_products


class BasketView(LoginRequiredMixin, ListView):
    model = basket
    template_name = 'shopping_cart.html'

    def get_context_data(self, **kwargs):
        context = super(BasketView, self).get_context_data(**kwargs)
        user_basket =  basket.objects.filter(Q(user = self.request.user), Q(is_active = True)).first()
        if user_basket:
            all_products = user_basket.items.all()
            context['baskets'] = all_products
        
        grand_total = 0
        products = basket_item.objects.filter(Q(user = self.request.user), Q(basket_items__is_active = True))
        for product in products:
            grand_total += product.get_subtotal()
        context['grand_total'] = grand_total
        return context