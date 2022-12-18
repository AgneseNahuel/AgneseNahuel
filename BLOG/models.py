from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

class comentarioM(models.Model):
    nombre= models.ForeignKey(User, on_delete=models.CASCADE)
    campo=models.TextField()
    date_created = models.DateTimeField(default=timezone.now())
    imagen =models.ImageField(upload_to="imagenBlog", null=True, blank=True)
    titulo=models.CharField(max_length=50, default="Sin Titulo")
    subtitulo=models.CharField(max_length=50, default="Sin Subtitulo")

    def __str__(self):
        return f"{self.nombre} - {self.campo} - {self.date_created}"
