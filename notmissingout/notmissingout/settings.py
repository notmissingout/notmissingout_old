"""
Django settings for notmissingout project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool("true" == os.environ.get("DJANGO_DEBUG", "false"))
TEMPLATE_DEBUG = DEBUG
DJANGO_DEBUG_TOOLBAR = (
    DEBUG and
    bool("true" == os.environ.get("DJANGO_DEBUG_TOOLBAR", "false"))
)

# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = '9g4z%=i76+d=-n9uxkb*o&ex79mo8bx_&8i!qp*p2@*kp91mhq'
else:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Who gets emails about site errors.
ADMINS = [
    ('Richard Boulton', 'richard@tartarus.org'),
]
MANAGERS = ADMINS

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'ideas4kids.org').split(';')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'cook',
    'sanitizer',
) + (('debug_toolbar',) if DJANGO_DEBUG_TOOLBAR else ())

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if DJANGO_DEBUG_TOOLBAR:
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'notmissingout.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'notmissingout.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

import dj_database_url
database = dj_database_url.config()
DATABASES = {
    'default': database
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, "uploaded_media")
MEDIA_URL = '/media/'


SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': True,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Change editor size
    'width': '100%',
    'height': '480',

    # Using Summernote Air-mode
    'airMode': False,

    # Customize toolbar buttons
    'toolbar': [
        ['undo', ['undo', 'redo']],
        ['style', [
            'style',
            'bold', 'italic', 'underline',
            'strikethrough', 'superscript', 'subscript',
            'color',
            'clear',
        ]],
        ['fontsize', ['fontsize', 'height']],
        ['para', ['ul', 'ol', 'paragraph', '']],
        ['insert', ['link', 'picture', 'table', 'hr']],
        ['extra', ['codeview', 'help']],
    ],

    # Need authentication while uploading attachments.
    'attachment_require_authentication': True,

    # Set `upload_to` function for attachments.
    #'attachment_upload_to': my_custom_upload_to_func(),

    # Set custom storage class for attachments.
    #'attachment_storage_class': 'my.custom.storage.class.name',

    # Set custom model for attachments (default: 'django_summernote.Attachment')
    #'attachment_model': 'my.custom.attachment.model', # must inherit 'django_summernote.AbstractAttachment'

    # Set common css/js media files
    'default_css': (
        '/static/bootstrap-3.3.7.min.css',
    ),
    'default_js': (
        '/static/jquery-1.12.4.min.js',
        '/static/bootstrap-3.3.7.min.js',
    ),
    'css': (
        '/static/django_summernote/summernote.css',
        '/static/codemirror-3.20.0/codemirror.css',
        '/static/codemirror-3.20.0/monokai.css',
    ),
    'js': (
        '/static/django_summernote/jquery.ui.widget.js',
        '/static/fileupload/load-image.all.min.js',
        '/static/fileupload/canvas-to-blob.min.js',
        '/static/fileupload/jquery.iframe-transport.js',
        '/static/fileupload/jquery.fileupload.js',
        '/static/fileupload/jquery.fileupload-process.js',
        '/static/fileupload/jquery.fileupload-image.js',
        '/static/fileupload/resize_image.js',
        '/static/codemirror-3.20.0/codemirror.js',
        '/static/codemirror-3.20.0/xml.js',
        '/static/codemirror-3.20.0/formatting.js',
        '/static/django_summernote/summernote.min.js',
    ),

    # And also for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
    'css_for_inplace': (
    ),
    'js_for_inplace': (
    ),

    # You can disable file upload feature.
    'disable_upload': False,

    # Codemirror as codeview
    'codemirror': {
        # Please visit http://summernote.org/examples/#codemirror-as-codeview
        'theme': 'monokai',
    },
}
