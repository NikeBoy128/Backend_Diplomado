from django.db import models

class Autos(models.Model):
    marca = models.CharField(max_length=50)
    cantidad_pasajeros=models.CharField(max_length=3)
    placa=models.CharField(max_length=10)
    imagen=models.ImageField(upload_to='autos/', null=True, blank=True)
    def __str__(self):
     return self.marca

class Viajes(models.Model):
    conductor=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    origen = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    auto = models.ForeignKey(Autos, on_delete=models.CASCADE)
    def __str__(self):
        return self.conductor.username
    
    

class Gastos(models.Model):
    viaje = models.ForeignKey(Viajes, related_name='gastos', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    imagen=models.ImageField(upload_to='gastos/', null=True, blank=True)
    def __str__(self):
        return self.descripcion