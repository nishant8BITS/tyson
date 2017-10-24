# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from views import forum, forum_subjects, subject_threads
from django.core.urlresolvers import resolve
from models import Thread, Subject, Post


# Testing the views

class BlogTest(TestCase):

    fixtures = ['threads', 'user']

    # Testing the main forum page
    def test_forum_page_resolves(self):
        forum_page = resolve('/forum/main')
        self.assertEqual(forum_page.func, forum)

    def test_forum_page__uses_right_template(self):
        forum_page = self.client.get('/forum/main')
        self.assertTemplateUsed(forum_page, "forum_main.html")

    def test_forum_page__contains_threads(self):
        forum_page = self.client.get('/forum/main', {'threads': Thread.objects.all()})
        self.assertContains(forum_page, 'Dog food or real food?') # check if page contains this thread name from the fixtures

    # Testing the page which contains the subjects
    def test_subject_page_resolves(self):
        subject_page = resolve('/forum/subjects')
        self.assertEqual(subject_page.func, forum_subjects)

    def test_subject_page__uses_right_template(self):
        subject_page = self.client.get('/forum/subjects')
        self.assertTemplateUsed(subject_page, "forumsubjects.html")

    def test_forum_page__contains_subjects(self):
        forum_page = self.client.get('/forum/subjects', {'subjects': Subject.objects.all()})
        self.assertContains(forum_page, 'Hobbies')  # check if page contains this subject name

    # Testing the view for threads with the same subject
    def test_threads_page_resolves(self):
        threads_page = resolve('/forum/threads/1/')
        self.assertEqual(threads_page.func, subject_threads)

    def test_threads_page__uses_right_template(self):
        threads_page = self.client.get('/forum/threads/2/')
        self.assertTemplateUsed(threads_page, "threads.html")

    def test_threads_page__contains_subject_and_thread(self):
        threads_page = self.client.get('/forum/threads/3/', {'threads': Thread.objects.all()})
        # check if page contains this thread name in subject with pk 3
        self.assertContains(threads_page, 'Do we really need humans?')
