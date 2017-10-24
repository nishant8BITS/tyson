from django.conf.urls import url
from views import post_list, post_detail


urlpatterns = [
    url(r'^blogposts/$', post_list, name='blogposts'),
    url(r'^blogposts/(?P<id>\d+)$', post_detail),
]