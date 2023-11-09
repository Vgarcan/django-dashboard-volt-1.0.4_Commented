from django.apps import AppConfig

class AppsConfig(AppConfig):
    """
    Configuración de la aplicación principal.

    Utiliza la clase base `AppConfig` de Django.
    Define el nombre y la etiqueta de la aplicación, y especifica el campo automático predeterminado.

    Attributes:
        default_auto_field (str): Especifica el tipo de campo automático predeterminado para modelos en la aplicación.
        name (str): Nombre de la aplicación.
        label (str): Etiqueta única para la aplicación.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps'
    label = 'apps'
