from django.conf.urls import url
from views import forum, forum_subjects, subject_threads, new_thread, thread, new_post, edit_post, delete_post

urlpatterns = [
    url(r'^main$', forum, name='forum_main'),
    url(r'^subjects$', forum_subjects, name='forum_subjects'),
    url(r'^subjects/(?P<subject_id>\d+)/$', subject_threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', delete_post, name='delete_post'),

]