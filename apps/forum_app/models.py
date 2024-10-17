from django.db import models
from django.utils import timezone
import random

# Create your models here.

class ForumPost(models.Model):
    titulo = models.CharField(max_length=40)
    autor = models.CharField(max_length=100,blank=True)
    text = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        # Atribuímos o valor aleatório para um autor não definido
        if not self.autor:
            number = random.randint(1, 2)
            match number:
                case 1:
                    self.autor = 'Cavalo Anônimo'

                case 2:
                    self.autor = 'Cervo Anônimo'

        super().save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(ForumPost, related_name='comentarios',on_delete=models.CASCADE,)
    autor = models.CharField(max_length=100,blank=True)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Atribuímos o valor aleatório para um autor não definido
        if not self.autor:
            number = random.randint(1, 4)
            match number:
                case 1:
                    self.autor = 'Cavalo Anônimo'

                case 2:
                    self.autor = 'Cervo Anônimo'
                
                case 3:
                    self.autor = 'Capivara Anônima'
                
                case 4:
                    self.autor = 'Falcão Anônimo'

        super().save(*args, **kwargs)

