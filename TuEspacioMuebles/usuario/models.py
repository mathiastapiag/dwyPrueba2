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


    #toString
    def __str__(self):
        return self.id_usuario+", " + self.username+", " + self.email+", " + self.genero+", " + self.fecha_nacimiento

    class Meta:
        ordering = ["id_usuario"]