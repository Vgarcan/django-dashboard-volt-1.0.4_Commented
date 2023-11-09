# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Importaciones necesarias desde Django
from django.urls import path, re_path

# Importación del módulo 'views' de la aplicación 'home'
from apps.home import views

# Lista de patrones de URL para la aplicación "home"
urlpatterns = [

    # Ruta para la página de inicio
    path('', views.index, name='home'),

    # Ruta que coincide con cualquier archivo HTML
    re_path(r'^.*\.*', views.pages, name='pages'),

]


# Modo de Empleo:
# - Este archivo 'urls.py' define las rutas URL asociadas con la aplicación "home" en tu proyecto Django.
# - La ruta '' (cadena vacía) está asociada a la función de vista 'index' en el módulo 'views'.
#   - Esta ruta se corresponde con la página de inicio de la aplicación.
# - La ruta 're_path(r'^.*\.*', views.pages, name='pages')' está asociada a la función de vista 'pages'.
#   - Esta ruta coincide con cualquier archivo HTML y llama a la función de vista 'pages'.
#   - Esto es útil para manejar rutas de archivos estáticos o páginas dinámicas no definidas explícitamente.
# - Asegúrate de que estas rutas estén correctamente configuradas en el archivo principal 'urls.py' del proyecto.

# Troubleshooting:
# - Verifica que las funciones de vista (index y pages) estén definidas en el módulo 'views.py' de la aplicación.
# - Si las rutas no funcionan como se esperaba, revisa el archivo principal 'urls.py' del proyecto para asegurarte
#   de que estas rutas estén incluidas y configuradas correctamente.









