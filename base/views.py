from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _

from .models import Product, Company

def home(request):
    products = get_translated_products()  # Получаем переведенные продукты для главной страницы
    company_info = get_company_info()
    return render(request, 'home.html', {'products': products, 'company_info': company_info})

def products(request):
    products = get_translated_products()  # Получаем переведенные продукты для страницы списка продуктов
    company_info = get_company_info()
    return render(request, 'products.html', {'products': products, 'company_info': company_info})

def contacts(request):
    company_info = get_company_info()
    return render(request, 'contacts.html', {'company_info': company_info})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)  # Получаем продукт по id или возвращаем 404
    company_info = get_company_info()
    return render(request, 'product_detail.html', {'product': product, 'company_info': company_info})


def get_translated_products():
    products = Product.objects.all()
    for product in products:
        product.name = _(product.name)
        product.description = _(product.description)
    return products

def get_company_info():
    company_info = Company.objects.first()
    return company_info
