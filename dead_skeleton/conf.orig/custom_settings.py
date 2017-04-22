# -*- coding: utf-8 -*-

import os
import datetime

from django.core.urlresolvers import reverse_lazy
from django.contrib.messages import constants as message_constants

# ------------------------------------------------------------
# General parameters
# ------------------------------------------------------------

# slug string
SLUG = "SLUG_PLACEHOLDER"

# admin
ADMIN_TITLE = u"SHORT_TITLE_PLACEHOLDER"
SHOW_ADMIN_TITLE = True

# window
WINDOW_TITLE = u"LONG_TITLE_PLACEHOLDER"

# navbar
NAVBAR_TITLE = u"SHORT_TITLE_PLACEHOLDER"
SHOW_NAVBAR_TITLE = True

# footer
SHOW_FOOTER_GO_UP = True
SHOW_FOOTER_GO_DOWN = True
SHOW_FOOTER_REFRESH = True
SHOW_FOOTER_LEFT_TITLE = True
SHOW_FOOTER_RIGHT_TITLE = True
SHOW_FOOTER_CONTAINER_MODE_SELECTOR = True

FOOTER_LEFT_TITLE = u"LONG_TITLE_PLACEHOLDER"

FOOTER_RIGHT_TITLE = u"Todos los derechos reservados &copy; {}".format(
    datetime.datetime.now().year
)

# email
EMAIL_CONTACT_SUBJECT = u"Nuevo mensaje contáctenos ({})"

# base template (skin)
BASE_TEMPLATE = "dead-common/skins/default/base.html"

# ------------------------------------------------------------
# Environment
# ------------------------------------------------------------

RUNNING_ENVIRONMENT_DEV = 1
RUNNING_ENVIRONMENT_TEST = 2
RUNNING_ENVIRONMENT_PRODUCTION = 3
RUNNING_ENVIRONMENT = RUNNING_ENVIRONMENT_DEV

# ------------------------------------------------------------
# Builtins
# ------------------------------------------------------------

TEMPLATES[0]['OPTIONS']['builtins'] = [
    'django.templatetags.static',
    'crispy_forms.templatetags.crispy_forms_tags',
    'dead_common.templatetags.filters',
]

# ------------------------------------------------------------
# Context processors
# ------------------------------------------------------------

TEMPLATES[0]["OPTIONS"]["context_processors"] += [
    'django.template.context_processors.media',
    'dead_common.context_processors.current_application_and_view',
    'dead_common.context_processors.basic',
]

# ------------------------------------------------------------
# Debug
# ------------------------------------------------------------

DEBUG = False if RUNNING_ENVIRONMENT != RUNNING_ENVIRONMENT_DEV else True

# ------------------------------------------------------------
# Allowed hosts
# ------------------------------------------------------------

if RUNNING_ENVIRONMENT == RUNNING_ENVIRONMENT_TEST:
    ALLOWED_HOSTS = [
        'SLUG_PLACEHOLDER.000cortazar000.pes',
        'www.SLUG_PLACEHOLDER.000cortazar000.pes',
    ]
elif RUNNING_ENVIRONMENT == RUNNING_ENVIRONMENT_PRODUCTION:
    ALLOWED_HOSTS = [
        'DOMAIN_PLACEHOLDER',
        'www.DOMAIN_PLACEHOLDER',
    ]
else:
    ALLOWED_HOSTS = [
        '192.168.0.19'
    ]

# ------------------------------------------------------------
# Apps
# ------------------------------------------------------------

INSTALLED_APPS = [
    'dal',
    'dal_select2',
] + INSTALLED_APPS

INSTALLED_APPS += [
    'crispy_forms',
    'captcha',
    'smart_selects',
    'import_export',
    'rangefilter',
    'adminfilters',
    'salmonella',
]

INSTALLED_APPS += [
    'applications.common',
    'applications.home',
]

INSTALLED_APPS += [
    'dead_common',
    'dead_js_utilities',
    'dead_forms',
]

INSTALLED_APPS += [
    'django.contrib.sites',
    'django.contrib.humanize',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

# ------------------------------------------------------------
# Site
# ------------------------------------------------------------

SITE_ID = 1

# ------------------------------------------------------------
# Databases
# ------------------------------------------------------------

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'NAME': os.path.join(BASE_DIR, 'db', '{}.db'.format(SLUG)),
   }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': SLUG,
#         'USER': 'postgres',
#         'PASSWORD': 'alonso',
#         'HOST': 'localhost'
#     }
# }

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': SLUG,
#        'USER': 'root',
#        'PASSWORD': 'xxx' if RUNNING_ENVIRONMENT != RUNNING_ENVIRONMENT_DEV else 'alonso',
#        'HOST': 'localhost'
#    }
#}

# ------------------------------------------------------------
# Localization
# ------------------------------------------------------------

LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ------------------------------------------------------------
# Static / Media
# ------------------------------------------------------------

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_URL = '/{}_static/'.format(SLUG)
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/{}_media/'.format(SLUG)

# ------------------------------------------------------------
# Crispy form
# ------------------------------------------------------------

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

# ------------------------------------------------------------
# Authentication
# ------------------------------------------------------------

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = reverse_lazy('home')
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_SUBJECT_PREFIX = u"[{}] ".format(SLUG)
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SESSION_REMEMBER = False
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
DISABLE_REGISTER = True

# Disable register
# if DISABLE_REGISTER:
#     ACCOUNT_ADAPTER = 'dead_users.account_adapter.DisabledSignupAccountAdapter'

# Enable first_name and last_name in signup
# ACCOUNT_SIGNUP_FORM_CLASS = 'dead_users.forms.SignupForm'

PRIMARY_IDENTITY_FIELD = "email"

# ------------------------------------------------------------
# Email settings
# ------------------------------------------------------------

if RUNNING_ENVIRONMENT == RUNNING_ENVIRONMENT_PRODUCTION:
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'EMAIL_USER_PLACEHOLDER'
    EMAIL_HOST_PASSWORD = 'EMAIL_PASSWORD_PLACEHOLDER'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = u'SLUG_PLACEHOLDER <EMAIL_USER_PLACEHOLDER>'
    SERVER_EMAIL = "EMAIL_USER_PLACEHOLDER"

    DEFAULT_BCC_RECIPIENTS = [
        'EMAIL_BCC_RECIPIENT_PLACEHOLDER',
    ]

elif RUNNING_ENVIRONMENT == RUNNING_ENVIRONMENT_TEST:
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'EMAIL_USER_PLACEHOLDER'
    EMAIL_HOST_PASSWORD = 'EMAIL_PASSWORD_PLACEHOLDER'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = u'SLUG_PLACEHOLDER <EMAIL_USER_PLACEHOLDER>'
    SERVER_EMAIL = "EMAIL_USER_PLACEHOLDER"

    DEFAULT_BCC_RECIPIENTS = [
        'EMAIL_BCC_RECIPIENT_PLACEHOLDER',
    ]

elif RUNNING_ENVIRONMENT == RUNNING_ENVIRONMENT_DEV:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'temporal')

    DEFAULT_BCC_RECIPIENTS = [
        'EMAIL_BCC_RECIPIENT_PLACEHOLDER',
    ]

EMAIL_ENABLED = True

ADMINS =[
    ('System Administrator', 'EMAIL_BCC_RECIPIENT_PLACEHOLDER'),
]

MANAGERS =[
    ('System Administrator', 'EMAIL_BCC_RECIPIENT_PLACEHOLDER'),
]

EMAIL_SUBJECT_PREFIX = u"[{}] ".format(SLUG)

# ------------------------------------------------------------
# Captcha
# ------------------------------------------------------------

CAPTCHA_FONT_SIZE = 40
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'

# ------------------------------------------------------------
# Smart selects
# ------------------------------------------------------------

USE_DJANGO_JQUERY = False
JQUERY_URL = STATIC_URL + 'externals/jquery/dist/jquery.min.js'

# ------------------------------------------------------------
# Messages framework
# ------------------------------------------------------------

MESSAGE_TAGS = {
    message_constants.DEBUG: 'debug',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}

# ------------------------------------------------------------
# Middlewares
# ------------------------------------------------------------

MIDDLEWARE += (
    'crum.CurrentRequestUserMiddleware',
)