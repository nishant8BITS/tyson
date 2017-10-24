# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Product


# Create our view to list the products
def all_products(request):
    products = Product.objects.all()
    return render(request, "products_list.html", {"products": products})
