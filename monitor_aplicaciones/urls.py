"""
URL configuration for monitor_aplicaciones project.

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
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('api_list')  # Redirige a la lista de APIs si está autenticado
    else:
        return redirect('login')  # Redirige a la página de login si no está autenticado

urlpatterns = [
    path('', home_redirect, name='home'),
    path("admin/", admin.site.urls),
    path('users/', include('users.urls')),
    path('apis/', include('api_monitor.urls')),
]
