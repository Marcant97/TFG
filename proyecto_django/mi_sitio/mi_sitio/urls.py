from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('formulario/', views.mi_vista, name='mi_vista'),
    path('admin/', admin.site.urls),
    path('enviar/', views.vista_enviar, name='vista_enviar')
]
