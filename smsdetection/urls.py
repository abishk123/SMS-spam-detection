"""
URL configuration for smsdetection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Imports the admin functionality from Django's built-in admin interface
from django.contrib import admin

# Imports the path function which is used to define URL patterns
from django.urls import path

# Imports all views from the detection app's views.py file
from detection.views import *

# urlpatterns list contains all URL patterns for the project
urlpatterns = [
    # Creates admin panel URL at '/admin/' - Django's built-in admin interface
    path('admin/', admin.site.urls),
    
    # Creates URL for message classification at '/classify_message/'
    # Links to classify_message view function from views.py
    path('classify_message/', classify_message, name='classify_message'),
    
    # Root URL ('') also points to classify_message view
    # This makes the classification page the homepage
    path('', classify_message, name='home'),
]