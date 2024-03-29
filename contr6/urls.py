"""contr6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from webapp.views import index_view, visitor_view, visitor_create_view, visitor_update_view, \
    visitor_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('visitor/<int:pk>/', visitor_view, name='visitor_view'),
    path('visitor/add/', visitor_create_view, name='visitor_add'),
    path('visitor/<int:pk>/update/', visitor_update_view, name='visitor_update'),
    path('visitor/<int:pk>/delete/', visitor_delete_view, name='visitor_delete'),
]
