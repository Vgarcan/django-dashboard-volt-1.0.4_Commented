# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

from django.core.asgi import get_asgi_application

# Modo de Empleo:

# 1. Configuración del Entorno ASGI:
#    - Este archivo 'asgi.py' configura el servidor ASGI para el proyecto Django.
#    - ASGI (Asynchronous Server Gateway Interface) se utiliza para manejar conexiones de forma asíncrona, comúnmente en aplicaciones en tiempo real.

# 2. Configuración de la Aplicación ASGI de Django:
#    - Se establece la configuración de Django para el entorno ASGI utilizando 'DJANGO_SETTINGS_MODULE'.
#    - La variable 'DJANGO_SETTINGS_MODULE' apunta al módulo 'settings' de la aplicación 'core'.

# 3. Obtención de la Aplicación ASGI:
#    - La aplicación ASGI de Django se obtiene mediante 'get_asgi_application()'.
#    - Esta aplicación se utiliza para manejar conexiones ASGI y ejecutar la lógica de la aplicación Django.

# Posibles Troubleshooting:

# 1. Problemas con la Configuración del Entorno ASGI:
#    - Si se encuentran errores relacionados con el entorno ASGI, verifica que 'DJANGO_SETTINGS_MODULE' esté configurado correctamente.
#    - Asegúrate de que la configuración de Django se encuentre en el lugar correcto y sea accesible.

# 2. Errores al Obtener la Aplicación ASGI:
#    - Si hay problemas al obtener la aplicación ASGI, revisa la configuración de 'application' y asegúrate de que se haya obtenido correctamente utilizando 'get_asgi_application'.
#    - Verifica que la configuración de la aplicación Django esté completa y correcta.

# 3. Considera leer los comentarios en el código para obtener información adicional y soluciones a problemas comunes.

# Establecer la configuración de Django para el entorno ASGI
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Obtener la aplicación ASGI de Django
application = get_asgi_application()
