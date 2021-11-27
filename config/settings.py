from pathlib import Path
import os



BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-ej8vo#nkrka1-3v*96_laut54h+hmu9ve@wmfnfd^nbydc$9x%'


DEBUG = True

ALLOWED_HOSTS = []



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages', # نیازی به تیبل دیتابیس ندارد
    'django.contrib.staticfiles', # نیازی به تیبل دیتابیس ندارد
    # ckeditor
    'ckeditor',
    'ckeditor_uploader',

    # Our Application
    'blog.apps.BlogConfig',
    'accounts.apps.AccountsConfig',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



ROOT_URLCONF = 'config.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



WSGI_APPLICATION = 'config.wsgi.application'



AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.authenticate.EmailAuthBackend',
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'

# زمانی که فایل های استیتک مربوط به کل اپلیکیشن هست نه یک اپ خاص از این اتربیوت استفاده میکنیم
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), # جنگو به اولین آدرسی که پیدا کرد، همونو لود میکنه و سراغ بقیه نخواهد رفت
]


# Media File: فایل هایی که زمان پروداکشن به پروژه افزوده میشه، می گویند
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') # آدرسی که قراره فایل های مدیا در اون ذخیره بشوند(ثابت است)
MEDIA_URL = '/media/' # آدرسی که جنگو از اون برای نمایش فایل ها از اون استفاده میکنه



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Ckeditor
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'full',
    },
}
CKEDITOR_UPLOAD_PATH = "uploads/" # Use Media Url and Media Root