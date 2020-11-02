from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('listar', views.listar, name='listar'),
    path('mostrar_alumnos', views.mostrar_alumnos, name='mostrar_alumnos'),
    path('buscar', views.buscar, name='buscar'),
    path('buscar_por_rut', views.buscar_por_rut, name='buscar_por_rut'),
    path('eliminar', views.eliminar, name='eliminar'),
    path('eliminar_por_rut', views.eliminar_por_rut, name='eliminar_por_rut'),
    path('agregar', views.agregar, name='agregar'),
    path('agregar_alumno', views.agregar_alumno, name='agregar_alumno'),

    path('modificar', views.modificar, name='modificar'),
    path('modificar_por_rut', views.modificar_por_rut, name='modificar_por_rut'),
    path('modificar_datos', views.modificar_datos, name='modificar_datos'),
    path('editar_alumno', views.editar_alumno, name='editar_alumno'),

    path('menu', views.menu, name='menu'), #alumnos
    path('menu_productos', views.menu_productos, name='menu_productos'),


]
