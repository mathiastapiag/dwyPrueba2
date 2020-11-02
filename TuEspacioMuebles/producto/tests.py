from django.test import TestCase
# Create your tests here.
import unittest
from producto.models import Producto


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
