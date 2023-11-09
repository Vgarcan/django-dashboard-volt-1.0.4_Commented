# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Importar módulos necesarios
import os
from decouple import config
from unipath import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Configuración de rutas base
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
# Configuración de la clave secreta
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
# Configuración del modo de depuración
DEBUG = config('DEBUG', default=True, cast=bool)

# load production server from .env
# Configuración de los hosts permitidos
ALLOWED_HOSTS = ['localhost', '127.0.0.1', config('SERVER', default='127.0.0.1')]

# Application definition
# Configuración de aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.home'  # Habilitar la aplicación interna 'home'
]

# Configuración de middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de la URL principal
ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Ruta definida en home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Ruta definida en home/urls.py

# Configuración del directorio de plantillas
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

# Configuración de la aplicación WSGI
WSGI_APPLICATION = 'core.wsgi.application'

# Database
# Configuración de la base de datos (SQLite en este caso)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Password validation
# Configuración de la validación de contraseñas
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
# Configuración de internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#############################################################
# Configuración de archivos estáticos

# Static files (CSS, JavaScript, Images)
# Configuración de archivos estáticos (CSS, JavaScript, imágenes)
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
# Directorios adicionales para que collectstatic encuentre archivos estáticos
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)

# Fin de la configuración
#############################################################

# Modo de Empleo:

# 1. Configuración de Rutas:
#    - `BASE_DIR` y `CORE_DIR` se utilizan para construir rutas a directorios dentro del proyecto.
#    - `BASE_DIR` representa el directorio del archivo actual, mientras que `CORE_DIR` representa el directorio anterior al directorio de este archivo.
#    - Estas variables facilitan la construcción de rutas a otros directorios del proyecto.

# 2. Clave Secreta y Modo de Depuración:
#    - La `SECRET_KEY` se utiliza para proporcionar una clave secreta para la aplicación Django.
#    - `DEBUG` determina si la aplicación se ejecuta en modo de depuración. En producción, se recomienda establecerlo en `False` para mayor seguridad.

# 3. Configuración de Hosts Permitidos:
#    - `ALLOWED_HOSTS` especifica qué hosts pueden acceder a la aplicación.
#    - Los hosts permitidos deben definirse en una lista y pueden provenir de la configuración o de un valor predeterminado.

# 4. Aplicaciones Instaladas y Middleware:
#    - `INSTALLED_APPS` lista las aplicaciones instaladas en el proyecto.
#    - `MIDDLEWARE` especifica el middleware utilizado en la aplicación Django.

# 5. Configuración de la URL Principal:
#    - `ROOT_URLCONF` establece la URL principal para enrutar las solicitudes.
#    - `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` definen las rutas a las que se redirigirá al usuario después de iniciar o cerrar sesión.

# 6. Configuración de Plantillas:
#    - `TEMPLATE_DIR` representa el directorio de plantillas.
#    - `TEMPLATES` configura el motor de plantillas de Django.

# 7. Configuración de la Aplicación WSGI y URL Principal:
#    - `WSGI_APPLICATION` apunta a la aplicación WSGI de la aplicación Django.

# 8. Configuración de la Base de Datos y Validación de Contraseñas:
#    - `DATABASES` configura la base de datos (SQLite en este caso).
#    - `AUTH_PASSWORD_VALIDATORS` establece las reglas de validación de contraseñas.

# 9. Configuración de Internacionalización:
#    - `LANGUAGE_CODE`, `TIME_ZONE`, `USE_I18N`, `USE_L10N` y `USE_TZ` configuran la internacionalización y la zona horaria.

# 10. Configuración de Archivos Estáticos:
#    - `STATIC_ROOT` y `STATIC_URL` definen la ubicación y la URL de los archivos estáticos recopilados.
#    - `STATICFILES_DIRS` especifica directorios adicionales donde se pueden encontrar archivos estáticos.

# Posibles Troubleshooting:

# 1. Error en Rutas:
#    - Asegúrate de que las rutas se construyan correctamente utilizando `BASE_DIR` y `CORE_DIR`.
#    - Si hay problemas con las rutas, verifica la configuración de estas variables y cómo se utilizan en el código.

# 2. Clave Secreta no Configurada:
#    - Si la `SECRET_KEY` no está configurada en el entorno o en el archivo `.env`, puede generar errores de seguridad.
#    - Configura una clave secreta única y segura en el entorno de producción.

# 3. Problemas con Hosts Permitidos:
#    - Si la aplicación no responde en determinados hosts, verifica que los hosts estén correctamente especificados en `ALLOWED_HOSTS`.

# 4. Errores en la Configuración de Aplicaciones o Middleware:
#    - Asegúrate de que las aplicaciones y el middleware estén configurados correctamente en `INSTALLED_APPS` y `MIDDLEWARE` respectivamente.

# 5. Configuración Incorrecta de la Base de Datos:
#    - Si la base de datos no funciona correctamente, verifica la configuración en `DATABASES` y asegúrate de que la base de datos esté creada.

# 6. Problemas con Archivos Estáticos:
#    - Si los archivos estáticos no se cargan correctamente, revisa la configuración de `STATIC_ROOT`, `STATIC_URL` y `STATICFILES_DIRS`.
#    - Asegúrate de que `whitenoise` esté configurado correctamente para manejar archivos estáticos en producción.

# 7. Errores de Internacionalización:
#    - Si hay problemas con la internacionalización, verifica las configuraciones relacionadas con el idioma y la zona horaria.

# 8. Errores en Configuración de Plantillas:
#    - Si hay problemas con las plantillas, asegúrate de que `TEMPLATE_DIR` esté configurado correctamente y que las plantillas estén ubicadas en el directorio correcto.

# 9. Problemas con Decouple:
#    - Asegúrate de que las variables de entorno estén configuradas correctamente en el archivo `.env` y se estén cargando correctamente usando `decouple`.

# 10. Errores de Whitenoise:
#    - Si estás utilizando `whitenoise`, asegúrate de que esté configurado adecuadamente para manejar archivos estáticos y comprimirlos en producción.

# 11. Considera leer los comentarios en el código para obtener información adicional y soluciones a problemas comunes.
