# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.core.urlresolvers import resolve
from views import all_products
from models import Product


class ProductsTest(TestCase):

    fixtures = ['products']

    def test_products_page_resolves(self):
        products_page = resolve('/products/products_list')
        self.assertEqual(products_page.func, all_products)

    def test_products_page_status_code_is_ok(self):
        products_page = self.client.get('/products/products_list')
        self.assertEqual(products_page.status_code, 200)

    def test_products_page__uses_right_template(self):
        products_page = self.client.get('/products/products_list')
        self.assertTemplateUsed(products_page, "products_list.html")

    def test_products_page__contains_products(self):
        products_page = self.client.get('/products/products_list', {'product': Product.objects.all()})
        # check if this product name is on products page
        self.assertContains(products_page, 'Pathfinder Adventure Cardgame')
        # check if this part of product description is on products page
        self.assertContains(products_page, 'Check out this blanket')