from django.contrib import admin
from .models import Product, Company

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available',)
    search_fields = ('name', 'description')
    
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    search_fields = ('name', 'phone_number', 'email')

admin.site.register(Product, ProductAdmin)
admin.site.register(Company, CompanyAdmin)