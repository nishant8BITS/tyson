from settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# PayPal Settings
SITE_URL = 'https://lulus-dog-forum.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://lulus-dog-forum.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'lulubusiness@gmail.com'