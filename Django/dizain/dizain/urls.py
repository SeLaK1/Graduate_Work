"""
URL configuration for dizain project.

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
from django.contrib import admin
from django.urls import path
from dizain_app.views import main, exampl, servis, registration, contacts, vhod

urlpatterns = [
    path('', main),
    path('main/exampl', exampl),
    path('main/services', servis),
    path('main/registration', registration),
    path('main/contacts', contacts),
    path('main/entrance', vhod),
]
