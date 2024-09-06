from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]