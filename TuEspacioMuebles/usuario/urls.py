from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    #Usuario
    path('index', views.index, name='index'),
    path('mision', views.mision, name='mision'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('login', views.login, name='login'),

    #Producto
    path('agregar_producto', views.agregar_producto, name='agregar_producto'),
    path('listar_producto', views.listar_producto, name='listar_producto'),
    path('eliminar_producto/<id>/', views.eliminar_producto, name='eliminar_producto'),
    path('modificar_producto/<id>/', views.modificar_producto, name='modificar_producto'),

]
