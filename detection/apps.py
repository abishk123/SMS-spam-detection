# Import the AppConfig class from Django's app configuration system
from django.apps import AppConfig

# Define the configuration class for the 'detection' app
class DetectionConfig(AppConfig):
    # Specifies the primary key field type for models in this app
    # BigAutoField is a 64-bit integer, allowing for many entries
    default_auto_field = 'django.db.models.BigAutoField'
    # The name of the app - must match the directory name
    # This is how Django identifies and references this app
    name = 'detection'
