from django.contrib import admin
from .models import Product, Offer, Author


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Author, AuthorAdmin)
