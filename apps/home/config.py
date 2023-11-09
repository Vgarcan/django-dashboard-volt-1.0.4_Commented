# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Importación de la clase base AppConfig desde el módulo django.apps
from django.apps import AppConfig

# Definición de la configuración de la aplicación
class MyConfig(AppConfig):
    """
    Configuración personalizada para la aplicación 'home'.

    Utiliza la clase base `AppConfig` de Django.
    Define el nombre y la etiqueta de la aplicación.

    Atributos:
        name (str): Nombre de la aplicación.
        label (str): Etiqueta única para la aplicación.
    """
    name = 'apps.home'
    label = 'apps_home'
