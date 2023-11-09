# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Importaciones necesarias de Django
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Decorador de Django para requerir autenticación antes de acceder a las vistas
@login_required(login_url="/login/")
def index(request):
    """
    Vista para la página de inicio.

    Requiere autenticación utilizando el decorador `@login_required`.
    Muestra la página principal ('home/index.html') con un contexto.

    Args:
        request (HttpRequest): Objeto de solicitud de Django.

    Returns:
        HttpResponse: Respuesta HTTP que renderiza la página de inicio.
    """
    # Crear un contexto para pasar datos al template
    context = {'segment': 'index'}

    # Obtener el template HTML para la página principal
    html_template = loader.get_template('home/index.html')

    # Renderizar el template con el contexto y devolver como HttpResponse
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    """
    Vista para páginas dinámicas.

    Requiere autenticación utilizando el decorador `@login_required`.
    Muestra páginas dinámicas basadas en la URL.

    Args:
        request (HttpRequest): Objeto de solicitud de Django.

    Returns:
        HttpResponse: Respuesta HTTP que renderiza la página solicitada.
    """
    # Inicializar el contexto como un diccionario vacío
    context = {}

    try:
        # Extraer el nombre del template de la última parte de la URL
        load_template = request.path.split('/')[-1]

        # Si la URL termina en 'admin', redireccionar a la página de administrador
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))

        # Agregar el nombre del template al contexto
        context['segment'] = load_template

        # Obtener el template HTML para la página solicitada
        html_template = loader.get_template('home/' + load_template)

        # Renderizar el template con el contexto y devolver como HttpResponse
        return HttpResponse(html_template.render(context, request))

    # Manejar el caso en que el template no existe
    except template.TemplateDoesNotExist:
        # Si el template no existe, cargar una página de error 404
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    # Manejar otros errores
    except Exception as e:
        # Si ocurre cualquier otra excepción, cargar una página de error 500
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Importaciones necesarias de Django
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Decorador de Django para requerir autenticación antes de acceder a las vistas
@login_required(login_url="/login/")
def index(request):
    """
    Vista para la página de inicio.

    Requiere autenticación utilizando el decorador `@login_required`.
    Muestra la página principal ('home/index.html') con un contexto.

    Args:
        request (HttpRequest): Objeto de solicitud de Django.

    Returns:
        HttpResponse: Respuesta HTTP que renderiza la página de inicio.
    """
    # Crear un contexto para pasar datos al template
    context = {'segment': 'index'}

    # Obtener el template HTML para la página principal
    html_template = loader.get_template('home/index.html')

    # Renderizar el template con el contexto y devolver como HttpResponse
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    """
    Vista para páginas dinámicas.

    Requiere autenticación utilizando el decorador `@login_required`.
    Muestra páginas dinámicas basadas en la URL.

    Args:
        request (HttpRequest): Objeto de solicitud de Django.

    Returns:
        HttpResponse: Respuesta HTTP que renderiza la página solicitada.
    """
    # Inicializar el contexto como un diccionario vacío
    context = {}

    try:
        # Extraer el nombre del template de la última parte de la URL
        load_template = request.path.split('/')[-1]

        # Si la URL termina en 'admin', redireccionar a la página de administrador
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))

        # Agregar el nombre del template al contexto
        context['segment'] = load_template

        # Obtener el template HTML para la página solicitada
        html_template = loader.get_template('home/' + load_template)

        # Renderizar el template con el contexto y devolver como HttpResponse
        return HttpResponse(html_template.render(context, request))

    # Manejar el caso en que el template no existe
    except template.TemplateDoesNotExist:
        # Si el template no existe, cargar una página de error 404
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    # Manejar otros errores
    except Exception as e:
        # Si ocurre cualquier otra excepción, cargar una página de error 500
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

# Modo de Empleo:
# - Estos son controladores de vistas de Django para la aplicación "home".
# - La función 'index' muestra la página de inicio, mientras que 'pages' maneja rutas dinámicas y muestra
#   páginas basadas en la URL.
# - Ambas funciones requieren autenticación, asegurando que solo los usuarios autenticados puedan acceder a estas vistas.
# - Se utilizan decoradores y utilidades de Django para cargar y renderizar templates HTML.
# - Asegúrate de que estas funciones estén correctamente configuradas en el archivo 'urls.py' de la aplicación "home".

# Troubleshooting:
# - Si las rutas no están funcionando, verifica que las funciones de vista (index y pages) estén definidas y
#   correctamente importadas en el archivo 'views.py' de la aplicación "home".
# - Asegúrate de que los templates HTML correspondientes estén presentes en la carpeta 'templates/home'.
# - Revisa las configuraciones de autenticación en tu proyecto para garantizar que el decorador 'login_required'
#   funcione correctamente.
