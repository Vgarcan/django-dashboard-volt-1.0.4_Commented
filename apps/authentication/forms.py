# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    """
    Formulario de inicio de sesión.

    Utiliza la clase base `forms.Form` de Django.
    Define campos para el nombre de usuario y la contraseña.

    Atributos:
        username (CharField): Campo para el nombre de usuario.
        password (CharField): Campo para la contraseña.
    """

    # Modo de Empleo:
    # - Utiliza este formulario para manejar el inicio de sesión de usuarios.
    # - El formulario contiene campos para el nombre de usuario y la contraseña.

    # Troubleshooting:
    # - Asegúrate de que este formulario se utilice en una vista adecuada para el inicio de sesión.
    # - Verifica que los atributos del formulario coincidan con los campos esperados en la vista asociada.

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    """
    Formulario de registro de usuario.

    Utiliza la clase base `UserCreationForm` de Django.
    Define campos para el nombre de usuario, correo electrónico y contraseña.

    Atributos:
        username (CharField): Campo para el nombre de usuario.
        email (EmailField): Campo para la dirección de correo electrónico.
        password1 (CharField): Campo para la contraseña.
        password2 (CharField): Campo para verificar la contraseña.
    """

    # Modo de Empleo:
    # - Utiliza este formulario para manejar el registro de nuevos usuarios.
    # - El formulario contiene campos para el nombre de usuario, correo electrónico y contraseña.

    # Troubleshooting:
    # - Asegúrate de que este formulario se utilice en una vista adecuada para el registro de usuarios.
    # - Verifica que los atributos del formulario coincidan con los campos esperados en la vista asociada.
    # - Comprueba que los campos de contraseña coincidan y cumplan con los requisitos de validación.

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        """
        Metaclase para configurar el formulario.

        Atributos:
            model (User): Modelo de usuario de Django.
            fields (tuple): Campos del formulario.
        """
        model = User
        fields = ('username', 'email', 'password1', 'password2')
