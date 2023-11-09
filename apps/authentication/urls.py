# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Importación de la función de vista 'LogoutView' desde el módulo 'django.contrib.auth.views'
from django.contrib.auth.views import LogoutView

# Importación de funciones y clases necesarias desde Django
from django.urls import path

# Importación de las funciones de vista 'login_view' y 'register_user' desde el módulo local .views
from .views import login_view, register_user

# Lista de patrones de URL para la gestión de autenticación de usuarios
urlpatterns = [
    # Ruta para la vista de inicio de sesión
    path('login/', login_view, name="login"),

    # Ruta para la vista de registro de usuarios
    path('register/', register_user, name="register"),

    # Ruta para la vista de cierre de sesión usando 'LogoutView' proporcionada por Django
    path("logout/", LogoutView.as_view(), name="logout")
]

# Instrucciones de Modo de Empleo:
# - Esta lista de urlpatterns define las rutas URL asociadas con la autenticación de usuarios.
# - '/login/' está asociado a la función de vista 'login_view' para manejar el inicio de sesión.
# - '/register/' está asociado a la función de vista 'register_user' para manejar el registro de usuarios.
# - '/logout/' está asociado a la vista 'LogoutView' para manejar el cierre de sesión.
# - Estas rutas son fundamentales para proporcionar funcionalidades de autenticación en la aplicación web Django.
# - Asegúrate de que estas rutas estén correctamente configuradas en el archivo principal 'urls.py' del proyecto.
