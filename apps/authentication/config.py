# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.apps import AppConfig

class AuthConfig(AppConfig):
    """
    Configuración de la aplicación de autenticación.

    Utiliza la clase base `AppConfig` de Django.
    Define el nombre y la etiqueta de la aplicación.

    Attributes:
        name (str): Nombre de la aplicación.
        label (str): Etiqueta única para la aplicación.
    """
    name = 'apps.auth'
    label = 'apps_auth'
