from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.

def home(request):
    products = getProducts()
    return render(request, 'home.html', {'products': products})

def products(request):
    products = getProducts()
    return render(request, 'products.html', {'products': products})

def contacts(request):
    return render(request, 'contacts.html')


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})



def getProducts():
    products = Product.objects.all()
    return products