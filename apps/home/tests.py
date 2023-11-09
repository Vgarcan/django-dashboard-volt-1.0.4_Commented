# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Importación de la clase base TestCase desde el módulo django.test
from django.test import TestCase

# Este archivo se utiliza para escribir pruebas unitarias para tu aplicación Django.

# Modo de Empleo:
# - Utiliza este archivo para escribir pruebas unitarias para las funciones y modelos de tu aplicación.
# - Define clases que hereden de `TestCase` y escriba métodos de prueba que verifiquen el comportamiento esperado.

# Troubleshooting:
# - Asegúrate de seguir la convención de nombres para las funciones de prueba. Deben comenzar con "test_".
# - Verifica que las pruebas aborden todos los casos posibles y proporcionen una cobertura adecuada.

# Ejemplo:
# class MiPrueba(TestCase):
#     def test_mi_funcion(self):
#         # ... código de prueba ...
#         self.assertEqual(resultado_actual, resultado_esperado)
