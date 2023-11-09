# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Registro de Modelos en el Panel de Administración de Django

# Modo de Empleo:

# 1. Propósito del Archivo:
#    - Este archivo 'admin.py' se utiliza para registrar modelos en el panel de administración de Django.

# 2. Registro de Modelos:
#    - Si tu aplicación tiene modelos definidos en 'models.py', deberías registrarlos aquí para poder gestionarlos
#      a través de la interfaz de administración de Django.
#    - Para registrar un modelo, utiliza la función 'admin.site.register(TuModelo)'.

# 3. Ejemplo:
#    - Si tienes un modelo llamado 'TuModelo' en el mismo directorio, puedes registrarlo así:
#        from .models import TuModelo
#        admin.site.register(TuModelo)

# Nota: Asegúrate de que los modelos estén correctamente definidos en 'models.py' antes de intentar registrarlos aquí.

# Ejemplo de Registro:
# from .models import TuModelo
# admin.site.register(TuModelo)
