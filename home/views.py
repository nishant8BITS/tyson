# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
def get_homepage(request):
    return render(request, 'index.html')


def get_aboutpage(request):
    return render(request, 'about.html')


def get_contactpage(request):
    return render(request, 'contact.html')