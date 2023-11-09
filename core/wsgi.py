# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from django.core.wsgi import get_wsgi_application

# Modo de Empleo:

# 1. Configuración del Archivo WSGI:
#    - Este archivo configura el servidor web para servir la aplicación Django.
#    - Utiliza el módulo `get_wsgi_application` de Django para obtener la aplicación WSGI.

# 2. Configuración del Entorno:
#    - Se establece la configuración del entorno de Django mediante la variable 'DJANGO_SETTINGS_MODULE'.
#    - Por defecto, se establece en 'core.settings', lo que indica que la configuración de Django se encuentra en el módulo 'settings' de la aplicación 'core'.

# 3. Aplicación WSGI:
#    - La variable 'application' se establece como la aplicación WSGI utilizando 'get_wsgi_application'.
#    - Esta aplicación se utiliza para gestionar las solicitudes HTTP y ejecutar la lógica de la aplicación Django.

# Posibles Troubleshooting:

# 1. Problemas con la Configuración del Entorno:
#    - Si hay errores relacionados con el entorno, verifica que 'DJANGO_SETTINGS_MODULE' esté configurado correctamente.
#    - Asegúrate de que la configuración de Django se encuentre en el lugar correcto y sea accesible.

# 2. Errores en la Aplicación WSGI:
#    - Si hay problemas con la aplicación WSGI, revisa la configuración de 'application' y asegúrate de que se haya obtenido correctamente utilizando 'get_wsgi_application'.
#    - Verifica que la configuración de la aplicación Django esté completa y correcta.

# 3. Considera leer los comentarios en el código para obtener información adicional y soluciones a problemas comunes.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
