from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    contenido = models.TextField(blank=True, null=True)
    fecha = models.DateField(default=timezone.now)
    autor = models.ForeignKey(User, null= True, on_delete= models.SET_NULL)
    image = models.ImageField(upload_to='blog_images/')  # Definimos el campo de imagen

    def __str__(self):
        return self.titulo
