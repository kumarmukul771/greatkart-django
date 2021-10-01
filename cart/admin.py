from django.contrib import admin
from .models import Cart2, CartItem2
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')


admin.site.register(Cart2, CartAdmin)
admin.site.register(CartItem2, CartItemAdmin)
