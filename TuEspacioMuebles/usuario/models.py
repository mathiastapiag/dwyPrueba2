from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario       = models.AutoField(db_column='id_usuario', primary_key=True)
    tipo_usuario     = models.IntegerField(blank=True, null=True) #0 -> Normal / 1 -> Admin
    fecha_nacimiento = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=100)
    username   = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    genero           = models.CharField(max_length=10, blank=True, null=True)
    foto             = models.ImageField(upload_to='fotos_usuario', blank=True, null=True)
    activo           = models.IntegerField(blank=True, null=True)


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

