# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from views import profile, login, logout, register
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from forms import UserRegistrationForm, UserLoginForm
from django import forms
from django.contrib.auth.models import User


# Testing the views

# Profile page tests

class ProfilePageTest(TestCase):
    def test_profile_page_resolves(self):
        profile_page = resolve('/account/profile/')
        self.assertEqual(profile_page.func, profile)

    def test_profile_page_status_code_is_ok(self):
        profile_page = self.client.get('/account/profile/')
        self.assertEqual(profile_page.status_code, 200)

    def test_check_content_is_correct(self):
        profile_page = self.client.get('/account/profile/')
        self.assertTemplateUsed(profile_page, "profile.html")
        profile_page_template_output = render_to_response("profile.html").content
        self.assertEqual(profile_page.content, profile_page_template_output)


# Registration page tests

class RegistrationPageTest(TestCase):
    def test_registration_page_resolves(self):
        registration_page = resolve('/account/register/')
        self.assertEqual(registration_page.func, register)

    def test_registration_page_status_code_is_ok(self):
        registration_page = self.client.get('/account/register/')
        self.assertEqual(registration_page.status_code, 200)

    def test_registration_page_uses_right_template(self):
        registration_page = self.client.get('/account/register/')
        self.assertTemplateUsed(registration_page, "register.html")


# Login page tests

class LoginPageTest(TestCase):
    def test_login_page_resolves(self):
        login_page = resolve('/account/login/')
        self.assertEqual(login_page.func, login)

    def test_login_page_status_code_is_ok(self):
        login_page = self.client.get('/account/login/')
        self.assertEqual(login_page.status_code, 200)

    def test_login_page_uses_right_template(self):
        login_page = self.client.get('/account/login/')
        self.assertTemplateUsed(login_page, "login.html")

# Logged-in view tests

class LoginTest(TestCase):

    # Create a user to test our logged-in view
    def setUp(self):
        super(LoginTest, self).setUp()
        self.user = User.objects.create(username='Tester')
        self.user.set_password('testing1')
        self.user.save()

    def test_login(self):
        logged_in = self.client.login(username='Tester', password='testing1')
        self.assertTrue(logged_in)

# Logout view tests

class LogoutViewTest(TestCase):
    def test_logout_request_resolves(self):
        logout_request = resolve('/account/logout/')
        self.assertEqual(logout_request.func, logout)

    def test_logout_request_status_code_is_ok(self):
        logout_request = self.client.get('/account/logout/')
        self.assertEqual(logout_request.status_code, 302)

    def test_logout_redirects_to_homepage(self):
        response = self.client.get('/account/logout/')
        self.assertRedirects(response, "/")


# Testing forms

class CustomUserTest(TestCase):

    # Registration form tests

    def test_registration_form(self):
        form = UserRegistrationForm({
            'username': 'Tester',
            'email': 'test@test.com',
            'password1': 'testing1',
            'password2': 'testing1'
        })

        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'username': 'Tester',
            'password1': 'testing1',
            'password2': 'testing1'
        })

        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_registration_form_fails_wih_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'username': 'Tester',
            'email': 'test@test.com',
            'password1': 'testing1',
            'password2': 'testing2'
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    # Login form tests

    def test_login_form(self):
        form = UserLoginForm({
            'username': 'Tester',
            'password': 'testing1'
        })

        self.assertTrue(form.is_valid())