from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Product, Company

# Create your views here.

def home(request):
    products = getProducts()
    company_info = get_company_info()
    return render(request, 'home.html', {'products': products, 'company_info': company_info, 'products': products})

def products(request):
    products = getProducts()
    company_info = get_company_info()
    return render(request, 'products.html', {'products': products, 'company_info': company_info})

def contacts(request):
    company_info = get_company_info()
    return render(request, 'contacts.html', {'company_info': company_info})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    company_info = get_company_info()
    return render(request, 'product_detail.html', {'product': product, 'company_info': company_info})

def getProducts():
    products = Product.objects.all()
    return products

def get_company_info():
    company_info = Company.objects.first()
    return company_info