# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # Añadir esta importación para incluir otras rutas

# Modo de Empleo:

# 1. Configuración de Rutas:
#    - Este archivo define las rutas principales del proyecto Django.
#    - Utiliza el módulo `admin` para la interfaz de administración de Django.
#    - Incluye rutas desde otras aplicaciones del proyecto usando `include`.

# 2. Ruta de Django Admin:
#    - La ruta '/admin/' está destinada a la interfaz de administración de Django.
#    - Accede a la interfaz de administración en la URL '/admin/'.

# 3. Rutas de Autenticación:
#    - Incluye las rutas de autenticación definidas en la aplicación 'authentication'.
#    - Estas rutas incluyen manejo de inicio de sesión, registro, etc.
#    - Están vinculadas a la URL base ("/") y se extienden desde allí.

# 4. Rutas de la Aplicación UI Kits:
#    - Incluye las rutas definidas en la aplicación 'home'.
#    - Estas rutas están destinadas a proporcionar archivos HTML para la interfaz de usuario.
#    - También se vinculan a la URL base ("/") y se extienden desde allí.

# Posibles Troubleshooting:

# 1. Error en las Rutas Incluidas:
#    - Si las rutas de otras aplicaciones no funcionan, verifica que las aplicaciones estén instaladas correctamente.
#    - Asegúrate de que los archivos 'urls.py' en 'authentication' y 'home' estén configurados correctamente.

# 2. Problemas con la Ruta de Django Admin:
#    - Si la interfaz de administración no está accesible en '/admin/', verifica la configuración de `admin.site.urls`.
#    - Asegúrate de que la aplicación 'admin' esté incluida en `INSTALLED_APPS`.

# 3. Errores en las Rutas de Autenticación:
#    - Si hay problemas con las rutas de autenticación, revisa las configuraciones en 'authentication/urls.py'.
#    - Verifica que las vistas de inicio de sesión, registro, etc., estén definidas correctamente.

# 4. Problemas con las Rutas de UI Kits:
#    - Si las rutas de la aplicación 'home' no cargan archivos HTML, verifica las configuraciones en 'home/urls.py'.
#    - Asegúrate de que las vistas y plantillas estén configuradas correctamente.



urlpatterns = [
    path('admin/', admin.site.urls),          # Ruta de administración de Django
    path("", include("apps.authentication.urls")), # Rutas de autenticación: inicio de sesión / registro
    path("", include("apps.home.urls"))             # Rutas de archivos HTML para UI Kits
]
