from django.conf.urls import url
from views import all_products


urlpatterns = [
    url(r'^products_list$', all_products, name='products_list')
]