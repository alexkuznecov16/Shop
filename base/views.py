import json
import os
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from .models import Product, Company
from django.db.models import Case, When
from base import models

def home(request):
    products = get_translated_products()  # Получаем переведенные продукты для главной страницы
    company_info = get_company_info()
    return render(request, 'home.html', {'products': products, 'company_info': company_info})

def products(request):
    sort_option = request.GET.get('sort', 'default')
    products = get_translated_products()
    
    if sort_option == 'price_asc':
        products = products.order_by('price')
    elif sort_option == 'price_desc':
        products = products.order_by('-price')
    elif sort_option == 'offer':
        special_offers = products.filter(offer=True)

        if special_offers.exists():
            products = special_offers.annotate(
                is_offer=Case(
                    When(offer=True, then=0),
                    When(offer=False, then=1),
                    output_field=models.IntegerField(),
                )
            ).order_by('is_offer', 'price')
        else:
            products = get_translated_products()

    company_info = get_company_info()
    return render(request, 'products.html', {
        'products': products,
        'company_info': company_info,
        'sort_option': sort_option,
    })

def contacts(request):
    company_info = get_company_info()
    return render(request, 'contacts.html', {'company_info': company_info})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)  # Получаем продукт по id или возвращаем 404
    company_info = get_company_info()
    return render(request, 'product_detail.html', {'product': product, 'company_info': company_info})


def get_translated_products():
    products = cache.get('cached_products')
    if products is None:
        products = []
        
        file_path = os.path.join('./files/example.json', 'products.json')
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                products_data = json.load(file)

            for product_data in products_data:
                product, created = Product.objects.get_or_create(
                    name=product_data['name'],
                    defaults={
                        'name_lv': product_data.get('name_lv', 'Standarts nosaukums'),
                        'description': product_data.get('description', 'Описание по умолчанию'),
                        'description_lv': product_data.get('description_lv', 'Standarts teksts'),
                        'price': product_data['price'],
                        'startPrice': product_data.get('startPrice', 0.00),
                        'available': product_data.get('available', True),
                        'offer': product_data.get('offer', False),
                        'image': product_data.get('image'),
                    }
                )

                if created:
                    print(f"Added new product: {product.name}")
                    
                product.name = _(product.name)
                product.description = _(product.description)
                products.append(product)

            cache.set('cached_products', products)
        else:
            print("File not found!")

    return products

def get_company_info():
    company_info = Company.objects.first()
    return company_info
