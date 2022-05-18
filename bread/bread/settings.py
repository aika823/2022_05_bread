import os
from pathlib import Path
import pymysql

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-!fvl)cd@s9zu8uafq4el*id^*da3gacl4sjxwp932oyni5#%jn'
DEBUG = True
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    # Custom Apps
    'app_manage',
    'app_api',
    'app_main',

    # Django Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]


# DJANGO ALLAUTH USER LOGIN AUTH
SITE_ID = 4
SOCIALACCOUNT_LOGIN_ON_GET = True
# ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_ADAPTER = 'app_main.adapter.MyAccountAdapter'
SOCIALACCOUNT_ADAPTER           = 'app_main.adapter.MySocialAccountAdapter'
SOCIALACCOUNT_AUTO_SIGNUP       = True  # 소셜로그인 시 자동으로 회원가입 처리
SIGNUP_REDIRECT_URL             = '/'   # 회원가입 시 이동하는 주소
LOGIN_REDIRECT_URL              = '/'   # 로그인 성공시 이동하는 주소
ACCOUNT_LOGOUT_ON_GET           = True  # 로그아웃 시 주소 이동 활성화
LOGOUT_REDIRECT_URL             = '/'   # 로그아웃 시 이동하는 주소
ACCOUNT_LOGOUT_REDIRECT_URL     = '/'   # 로그아웃 시 이동하는 주소
# ACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True #이메일 디폴트 설정

# 기존 유저 모델 수정
AUTH_USER_MODEL = 'app_main.User' 



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'bread.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')),],
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
WSGI_APPLICATION = 'bread.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default' : {
#         'ENGINE': 'django.db.backends.mysql',
#         # 'NAME': 'dbtarot',              
#         # 'USER': 'tarot',                      
#         # 'PASSWORD': 'bos210820@',              
#         # 'HOST': 'db.contest-activity.com',
#         'PORT': '3306',   
#         # 이모지 입력을 위한 옵션
#         'OPTIONS':{
#             'charset':'utf8mb4',
#             'use_unicode':True,
#         },
#     }
# }

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
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = False

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "static/css"),
    os.path.join(BASE_DIR, "static/images"),
    os.path.join(BASE_DIR, "static/js"),
    "static/css",
    "static/js",
    "static/images",
]

MEDIA_URL = "/media/"
MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, "media"),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'