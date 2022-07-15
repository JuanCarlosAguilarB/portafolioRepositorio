from .base import *
DEBUG = True

ALLOWED_HOSTS = ['djangoportfoliojuan.herokuapp.com']
                    

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'datigg9juk0hvc',
        'USER': 'kurdoxgwwwwgst',
        'PASSWORD': '709b9ede5dd8d7ab7020f326ba409f095f1ba85242e536daf8d6466103971f6e',
        'HOST': 'ec2-52-205-61-230.compute-1.amazonaws.com',
        'PORT': '',
    }
}

STATICFILES_DIRS = [(BASE_DIR, 'static'),]
