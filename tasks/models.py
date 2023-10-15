from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    titulo= models.CharField(max_length=100)
    
    descripcion=    models.TextField(blank=True)
    
    # auto_now_add en true lo que hace es que si no le definimos la fecha por defecto se va a autoasignar en el momento en que creamos la tupla
    fecha_creacion= models.DateTimeField(auto_now_add=True)
    
    completada= models.DateTimeField(null=True, blank=True)
    
    es_importante=  models.BooleanField(default=False)
    
    # debe ser clave foranea de usuario
    creada_por = models.ForeignKey(User ,on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.titulo + ' - Tarea de: --> '+ str(self.creada_por))
    


# el atributo blank en true significa que es opcional