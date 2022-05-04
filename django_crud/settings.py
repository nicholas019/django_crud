
from my_settings import SECRET_KEY, DATABASES
from pathlib import Path
# 프로젝트에서 사용할 경로설정  모듈
import pymysql

pymysql.install_as_MySQLdb()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY
# 프로젝트 생성시 자동생성
# 역할 : 서버에서만 사용하는 비밀키, 절대 외부 노출 금지, 회원정보까지 노출가능함, 노출되지 않는 곳에서 보관함.
# 환경번수를 import 해서 연결해서 사용한다.


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 디버깅모드 설정  배포시 False, 개발단계 True

ALLOWED_HOSTS = []
# 어떤 아이피가 서버에 접속허용할지 리스트형태로 설정 
# ALLOWED_HOSTS = ["접속허용할 아이피주소 입력"]

# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin', # 기본제공하는 관리자모드, 직접구현을을 할것임으로 주석처리
    # 'django.contrib.auth',  # 기본제공하는 인증기능, 직접구현을 할것임으로 주석처리
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders', # 보안을 위해 설치한 corsheaders app에 추가
    'health_check',
    'users',
]

# 프로젝트에서 추가한 app들을 추가한후에 여기에 꼭 입력해줘야한다.





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 보안을 위해 설치한 corsheaders 미들웨어에 추가
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',    # 기본제공하는 CSRF관련 미들웨어, 직접구현을 할것임으로 주석처리
    # 'django.contrib.auth.middleware.AuthenticationMiddleware', # 기본제공하는 인증 미들웨어, 직접구현을 할것임으로 주석처리
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

# 클라이언트로부터 받은 요청이 미들웨어를 지나서 url conf가 실행된다.  url로 들어오기전에 요청을 막고 방어하는 용도




ROOT_URLCONF = 'django_crud.urls'
# 루트 url을 결정하는 곳, 클라이언트의 요청이 들어왔을때 가장먼저 django_crud 폴더 에 있는 urls.py 폴더를 가장먼저 확인한다는 듯



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
            ],
        },
    },
]
# 이제 탬플릿을 사용하는 경우는 없다.



WSGI_APPLICATION = 'django_crud.wsgi.application'
# 나중에 설명 예정


DATABASES = DATABASES
# 어떤 DB를 사용할지 설정, 기본값 sqlist3 
# 환경병수는 따로 빼준다.



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.pSECRET_KEYassword_validation.UserAttributeSimilarityValidator',
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
# 장고에서 기본적으로 제공하는 유저모델 설정, 보통은 기본제공되는것을 안쓰고 직접 만들어서 쓴다.


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
# 시간관련된 처리를 할때 기준점



STATIC_URL = 'static/'
# 잘사용하지않는다. 파일을 연결할때 사용하는데 장고가 무거워지면안됨으로 따로 관리한다.


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



##CORS(보안) 관련 추가 설정사항 
## CORS설정을 하나하나 커스텀 하기위한 설정값
CORS_ORIGIN_ALLOW_ALL=True
# 모든 CORS 관련 요청에 열려있다.
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
# HTTP 프로토콜에서 발생하는 요청에서 발생하는 CORS문제를 메소드별로 설정가능하도록 설정 
# 여기에 등록되어있는 메소드만 받도록 하며 등록이 안되면 미드웨어에서 HTTP요청이 들어와도 URL로 못오고 미들웨어에서 막힘.

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
# 더 디테일한 메소드 설정 