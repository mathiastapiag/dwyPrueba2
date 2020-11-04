from django.test import TestCase
# Create your tests here.
import unittest
from usuario.models import Usuario
from usuario.models import Producto


class testUsuario(unittest.TestCase):

    def test_crear_objeto(self):
        usuario = Usuario.objects.create(
            tipo_usuario=0,
            fecha_nacimiento='2020-03-03',
            email='mathias.tapiag@gmail.com',
            username='mathias.tapiag',
            password='test123',
            genero='masculino',
            foto='',
            activo=1
                       )
        usuario.save()

        self.assertTrue(usuario,True)

class testProducto(unittest.TestCase):

    def test_crear_objeto(self):
        producto = Producto.objects.create(
                       nombre_producto='Agua Purificada Muy Buena',
                       precio='9990',
                       stock='20',
                       foto='',
                       activo=1
                       )
        producto.save()

        self.assertTrue(producto,True)
