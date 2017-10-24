# Dog Talk App

## Overview

A fictional website for dogs where they can talk to other dogs on the forum, read the blog of Loulou, or purchase dog related products

## Features

- Registration, Login, Logout
    - users can register on the site, log in and log out
- Forum 
    - visitors can read the threads on the Forum as well, but only registered users can comment or create new threads
- Blog
    - both visitors and registered users are able to read the blog
    - the blog can be updated only by the registered admin
- Products - users and visitors can buy products by using their paypal account
- About, Contact - these pages show additional information about the owner of the site

## Tech Used

- [Django](https://www.djangoproject.com/): a high-level Python-based framework for building web apps
	
- [Arrow](https://pypi.python.org/pypi/arrow): a Python library used for creating, manipulating, formatting and converting dates, times, and timestamps

- [Bootstrap](http://getbootstrap.com/): a HTML, CSS and JS framework for building responsive, mobile-first websites
	
- [TinyMCE](https://www.tinymce.com/): browser-based WYSIWYG text editor with the ability to convert HTML textarea fields or other HTML elements to editor instances. In our project we use ***tinyMCE*** to provide the users with a text editor to format their posts
- [Pillow](https://python-pillow.org/): a Python imaging library
	
## Testing

Different unittests were conducted using Django's testing framework. The unittests can be found in each app's tests.py file. The single payment function was tested by using the Paypal Test account created at https://developer.paypal.com/

