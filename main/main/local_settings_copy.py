from main.settings import *


STATIC_URL = 'static/'


STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home/gorills/project/avrora-bget/static/',
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# beget
STATIC_URL = 'static/'


STATIC_ROOT = '/home/a/avroraweb/avrora-new.avroraweb.beget.tech/public_html/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home/a/avroraweb/avrora-new.avroraweb.beget.tech/public_html/static/',
)
MEDIA_URL = 'media/'

MEDIA_ROOT = '/home/a/avroraweb/avrora-new.avroraweb.beget.tech/public_html/main/media/'

DEBUG = False

ALLOWED_HOSTS = ['avrora-new.avroraweb.beget.tech']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'OPTIONS': {
            'sql_mode': 'traditional',
        },
        'NAME': 'avroraweb_digita',
        'USER': 'avroraweb_digita',
        'PASSWORD': 'hViHROuu!1',
        'HOST': 'localhost',
        
    }
}

RECAPTCHA_PRIVATE_KEY = 'your private key'
RECAPTCHA_PUBLIC_KEY = 'your public key'
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5
RECAPTCHA_LANGUAGE = 'en' 



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.fullspace.ru' 
EMAIL_HOST_USER = 'info@maglena.tomsk.ru' 
EMAIL_HOST_PASSWORD = 'Ie51587v' 
EMAIL_PORT = 465 
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False


# for auto detection language, remove this from your settings
# If you require reCaptcha to be loaded from somewhere other than https://google.com
# (e.g. to bypass firewall restrictions), you can specify what proxy to use.
# RECAPTCHA_FRONTEND_PROXY_HOST = 'https://recaptcha.net'