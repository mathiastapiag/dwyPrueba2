from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto      = models.AutoField(db_column='id_producto', primary_key=True)
    #tipo_producto    = models.IntegerField(blank=True, null=True)
    nombre_producto  = models.CharField(max_length=50, blank=True, null=True)
    precio           = models.CharField(max_length=11, blank=True, null=True)
    stock            = models.CharField(max_length=9, blank=True, null=True)
    foto             = models.ImageField(upload_to='fotos_producto', blank=True, null=True)
    activo           = models.IntegerField(blank=True, null=True)

#class Tipo_Producto(models.Model):
  #  id_tipo_producto = models.AutoField(db_column='id_producto', primary_key=True)
   # tipo_producto = models.IntegerField(blank=True, null=True)
   # activo = models.IntegerField(blank=True, null=True)

    #toString
    def __str__(self):
        return self.id_producto+", " + self.nombre_producto+", " + self.precio+", " + self.stock

    class Meta:
        ordering = ["id_producto"]