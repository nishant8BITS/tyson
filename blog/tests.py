# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from views import post_list, post_detail
from django.core.urlresolvers import resolve
from models import Post


# Testing the views

class BlogTest(TestCase):

    fixtures = ['posts']

    # Testing the main blog page
    def test_blog_page_resolves(self):
        blog_page = resolve('/blog/blogposts/')
        self.assertEqual(blog_page.func, post_list)

    def test_blog_page_status_code_is_ok(self):
        blog_page = self.client.get('/blog/blogposts/')
        self.assertEqual(blog_page.status_code, 200)

    def test_blog_page__uses_right_template(self):
        blog_page = self.client.get('/blog/blogposts/', {'posts': Post.objects.all()})
        self.assertTemplateUsed(blog_page, "blogposts.html")

    def test_blog_page__contains_posts(self):
        blog_page = self.client.get('/blog/blogposts/', {'posts': Post.objects.all()})
        self.assertContains(blog_page, 'Watch out all doggies!') # check if page contains this blog title from the fixtures

    # Testing the page with the detailed blog post view
    def test_postdetail_page_resolves(self):
        postdetail_page = resolve('/blog/blogposts/2')
        self.assertEqual(postdetail_page.func, post_detail)

    def test_postdetail_page_status_code_is_ok(self):
        postdetail_page = self.client.get('/blog/blogposts/2')
        self.assertEqual(postdetail_page.status_code, 200)

    def test_postdetail_page__uses_right_template(self):
        postdetail_page = self.client.get('/blog/blogposts/2')
        self.assertTemplateUsed(postdetail_page, "postdetail.html")

    def test_postdetail_page__contains_postdetails(self):
        postdetail_page = self.client.get('/blog/blogposts/2')
        # check if the detailed post contains the last sentence
        self.assertContains(postdetail_page, 'Vivamus sodales nisl ut porta aliquet.')