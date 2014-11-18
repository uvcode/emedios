"""
Django settings for emedios project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's#4d=rl^h5(pbv)cys0j@t)b_7bnetcvzovc9-=nk$ibf-aqfp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'login',
    'multimedia',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'emedios.urls'

WSGI_APPLICATION = 'emedios.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
if bool(os.environ.get('LOCAL_DEV', True)): 
  DATABASES = {
    'default' : {
         'ENGINE' : 'django.db.backends.postgresql_psycopg2',
         'NAME' : 'db_emedios',
         'USER' : 'dennys',
         'PASSWORD' : '123456',
      }
  } 
else: 
  DATABASES = {
      'default' : dj_database_url.config(default='postrgres://localhost')
  }


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = ('%d-%m-%Y',)



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATIC_ROOT = 'staticfiles'
STATIC_URL = '/statics/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'statics'),
)

TEMPLATE_DIRS = (
    BASE_DIR,  'templates'
)

from django.core.urlresolvers import reverse_lazy

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = 'panel/'
LOGOUT_URL = reverse_lazy('login')

# -----------

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'login.context_processors.my_processor',
)

