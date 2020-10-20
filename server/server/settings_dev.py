from .settings import *
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aishare_test',
        'USER': 'root',
        'PASSWORD': 'woshitheone1F!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
