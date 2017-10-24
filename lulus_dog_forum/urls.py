"""know_your_owner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import views as home_views
from django.views.static import serve
from settings.dev import MEDIA_ROOT
from paypal.standard.ipn import urls as paypal_urls
from paypal_store.views import paypal_return, paypal_cancel


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_homepage, name='home'),
    url(r'^about/$', home_views.get_aboutpage, name='about'),
    url(r'^contact/$', home_views.get_contactpage, name='contact'),
    url(r'^account/', include('accounts.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}), # media urls for the blog images
    url(r'^forum/', include('forum.urls')),
    url(r'^products/', include('products.urls')),
    # paypal urls
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return$', paypal_return),
    url(r'^paypal-cancel$', paypal_cancel),
]
