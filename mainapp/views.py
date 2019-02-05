from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import ProductCategory, Product

import datetime


# Create your views here.
def index(request: HttpRequest):
    products = Product.objects.all()
    title = 'главная'
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

def products(request: HttpRequest, pk = None):
    print(pk)
    same_products = Product.objects.all()
    links_menu = ProductCategory.objects.all()
    title = 'каталог'

    if pk is not  None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = ('name', 'все')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
                'title': title,
                'links_menu': links_menu,
                'category': category,
                'products': products,
        }

        same_products = Product.objects.all()[3: 5]
        content = {
            'title': title,
            'links_menu': links_menu,
            'same_products': same_products
        }


    content = {'title': title,'same_products': same_products, 'links_menu': links_menu}
    return render(request, 'mainapp/products.html', content)

def contact(request: HttpRequest):
    title = 'контакты'
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/contact.html', content)

