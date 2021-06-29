# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-!n=qwgc!4!ce3g48)c-h-1chf*50bsf=!4it1!f@4pp%l98(!s'
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-!n=qwgc!4!ce3g48)c-h-1chf*50bsf=!4it1!f@4pp%l98(!s')