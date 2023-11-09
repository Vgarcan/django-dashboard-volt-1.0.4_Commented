# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Importaciones necesarias desde Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Importación de los formularios LoginForm y SignUpForm desde el módulo local .forms
from .forms import LoginForm, SignUpForm

# Vista para manejar el inicio de sesión
def login_view(request):
    """
    Maneja las solicitudes de inicio de sesión.
    - Utiliza el formulario LoginForm para autenticar al usuario.
    - Muestra un formulario de inicio de sesión en la página "/login/".
    - Si la autenticación es exitosa, redirige al usuario a la página principal ("/").
    - Si la autenticación falla, muestra un mensaje de credenciales inválidas.
    """
    # Crear una instancia del formulario LoginForm con los datos de la solicitud (si los hay)
    form = LoginForm(request.POST or None)

    # Variable para mensajes
    msg = None

    # Manejar solicitudes POST
    if request.method == "POST":
        # Verificar si el formulario es válido
        if form.is_valid():
            # Obtener datos del formulario
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            # Autenticar al usuario
            user = authenticate(username=username, password=password)

            # Verificar si la autenticación fue exitosa
            if user is not None:
                # Iniciar sesión y redirigir a la página principal
                login(request, user)
                return redirect("/")
            else:
                # Mostrar mensaje de credenciales inválidas si la autenticación falla
                msg = 'Invalid credentials'
        else:
            # Mostrar mensaje de error si el formulario no es válido
            msg = 'Error validating the form'

    # Renderizar la página de inicio de sesión con el formulario y el mensaje
    return render(request, "accounts/login.html", {"form": form, "msg": msg})


# Vista para manejar el registro de usuarios
def register_user(request):
    """
    Maneja las solicitudes de registro de nuevos usuarios.
    - Utiliza el formulario SignUpForm para registrar y autenticar al usuario.
    - Muestra un formulario de registro en la página "/register/".
    - Si el registro es exitoso, muestra un mensaje de éxito y redirige al usuario a la página de inicio de sesión ("/login/").
    - Si hay errores en el formulario, muestra un mensaje de error.
    """
    # Inicializar variables para mensajes y éxito
    msg = None
    success = False

    # Manejar solicitudes POST
    if request.method == "POST":
        # Crear una instancia del formulario SignUpForm con los datos de la solicitud
        form = SignUpForm(request.POST)
        # Verificar si el formulario es válido
        if form.is_valid():
            # Guardar el usuario en la base de datos
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")

            # Autenticar al usuario recién registrado
            user = authenticate(username=username, password=raw_password)

            # Configurar mensajes de éxito
            msg = 'User created - please <a href="/login">login</a>.'
            success = True
        else:
            # Mostrar mensaje si el formulario no es válido
            msg = 'Form is not valid'
    else:
        # En caso de solicitud GET, inicializar un nuevo formulario SignUpForm
        form = SignUpForm()

    # Renderizar la página de registro con el formulario, el mensaje y la indicación de éxito
    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
