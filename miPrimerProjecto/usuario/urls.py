from django.urls import path
from .views import listarUsuarios,registrarUsuario
urlpatterns = [
    path('',listarUsuarios,name = 'listarUsuario'),
    path('crear/',registrarUsuario, name = 'registrarUsuario')
]
