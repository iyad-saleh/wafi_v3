"""
Django settings for Aymen project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import environ
from django.utils.translation import gettext_lazy as _
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ROOT_DIR = environ.Path(__file__) - 3
# APPS_DIR = ROOT_DIR.path("apps")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gk4y-p)ek1r3jcuxg_(x*#hl%a@#wt_q=dl*h2kic!5+8cq91k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
AUTH_USER_MODEL = 'users.MyUser'
# Application definition

INSTALLED_APPS = [
    # 'jet.dashboard',
    # 'jet',
    # 'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    # 'jquery',
    # 'djangoformsetjs',
   'django_htmx',
    'mptt',
    'international',
    'crispy_forms',
    'widget_tweaks',
    'import_export',
    'django_extensions',

    "debug_toolbar",

    'taggit',#pip install django-taggit
    'ckeditor',  #pip install django-ckeditor
    'ckeditor_uploader',
    'dashboard',
    'common',
    'company',
    'account',
    # 'customer',
    # 'box',

    'passport',
    # 'employee',
    # 'bus',
    # 'expense',
    # 'trip',
    # 'reservation',
    'entry',
    # 'guest',
    # 'package',

    'airline',
      # General use templates & template tags (should appear first)
    # 'adminlte3',
     # Optional: Django admin theme (must be before django.contrib.admin)
    # 'adminlte3_theme',


]


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda r: False,  # disables it
    # '...
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",

]


ROOT_URLCONF = 'Aymen.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # 'django.contrib.auth.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Aymen.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGES = (
    # ('fr', 'Français'),
    # ('de', 'Deutsch'),
    ('en', _('English')),
    ('ar', _('Arabic')),
)
LANGUAGE_CODE = 'en-us'
LOCALE_PATHS = (
    BASE_DIR / 'locale/',
)
TIME_ZONE = 'Asia/Damascus'

USE_I18N = True

# USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    ]
STATIC_ROOT = 'static_media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH="ckeditor_uploads/"
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": "slate",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }
}


JAZZMIN_SETTINGS = {

"site_title": "Library Admin",
# Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if abse
"site_header": "Library",
# Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or N
"site_brand": "Library",
# Logo to use for your site, must be present in static files, used for brand on top left
"site_logo": "media/logo.png",
# Logo to use for your site, must be present in static files, used for login form logo (defaul
"login_logo": None,
# Logo to use for login form in dark themes (defaults to login_logo)
"login_logo_dark": None,
# CSS classes that are applied to the logo above
"site_logo_classes": "img-circle",
# Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32
"site_icon": None,
# Welcome text on the login screen
"welcome_sign": "Welcome to the library",
# Copyright on the footer
"copyright": "Eyad Library Ltd",
# The model admin to search from the search bar, search bar omitted if excluded
"search_model": "auth.User",
# Field name on user model that contains avatar ImageField/URLField/Charfield or a callable th
"user_avatar": None,

    "topmenu_links": [
# Url that gets reversed (Permissions can be added)
{"name": "Home", "url": "home"},
# model admin to link to (Permissions checked against model)
{"model": "auth.User"},
# App with dropdown menu to all its models pages (Permissions checked against models)
{"app": "company"},
{"app": "blog"},
    ],

# Additional links to include in the user menu on the top right ("app" url type is not allowed
"usermenu_links": [
    {"name": "Support",
     "url": "https://github.com/farridav/django-jazzmin/issues",
      "new_window":True},
    {"model": "auth.user"}
],

#############
# Side Menu #
#############
# Whether to display the side menu
"show_sidebar": True,
# Whether to aut expand the menu
"navigation_expanded": True,
# Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],
# Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
# List of apps (and/or models) to base side menu ordering off of (does not need to contain all
    "order_with_respect_to": ["auth", "blog", "company"],
# Custom links to append to app groups, keyed on app name
    # "custom_links": {
    # "books": [{
    # "name": "Make Messages",
    # "url": "make_messages",
    # "icon": "fas fa-comments",
    # "permissions": ["books.view_book"]
# }]
# },
# Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=
# for the full list of 5.13.0 free icon classes
"icons": {
"auth": "fas fa-users-cog",
"auth.user": "fas fa-user",
"auth.Group": "fas fa-users",
"company.company":"fas fa-box",
"company.companyType":"fas fa-object-group",
"customer.customer":"fas fa-registered",
"coin.coin":"fas fa-coins",
"passport.passport":"fas fa-passport",
"employee.employee":"fas fa-people-carry",
"bus.bus":"fas fa-bus",
"bus.driver":"fas fa-car",
"blog.post":"fas fa-blog",
"box.box":"fas fa-box-open",
"expense.expense":"fas fa-coffee",
"account.account":"fas fa-cash-register",
"ked.journal":"fas fa-journal-whills",
"ked.ked":"fas fa-address-book",
},
# Icons that are used when one is not manually specified
"default_icon_parents": "fas fa-chevron-circle-right",
"default_icon_children": "fas fa-circle",
#################
# Related Modal #
#################
# Use modals instead of popups
"related_modal_active": True,
"show_ui_builder": False,

# "language_chooser": True,

"changeform_format": "carousel",


}

CKEDITOR_CONFIGS = {
      'default': {
        # 'skin': 'moono',
        # 'skin': 'office2013',
        # 'skin': 'kama',
        'skin': 'moonocolor',
        # 'skin': 'moono-dark',
        # 'skin': 'bootstrapck',

        'toolbar_Custom': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Youtube','Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['CodeSnippet']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize','html5video',

            ]},
        ],
        'toolbar': 'Custom',  # put selected toolbar config here
        'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        'height': 400,
        # 'width': '100%',
        'filebrowserWindowHeight': 725,
        'filebrowserWindowWidth': 940,
        'toolbarCanCollapse': True,
        'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'codesnippet',
            'exportpdf',
            'colorbutton',
            'emoji',
             'html5video,widgetselection',
             'autocomplete',
             'textwatcher',
             'textmatch',
        ]),



    }
}