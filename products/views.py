from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Offer


def index(request):
    products = Product.objects.all()
    offers = Offer.objects.all()
    zipped_data = zip(products, offers)
    return render(request, 'index.html', {'zipped_data': zipped_data})


def cart(request):
    return HttpResponse('Product added to cart.')
