from django.db import models
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    imagem = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return self.titulo