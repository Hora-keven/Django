from django.db import models

# Create your models here.
class Pessoas(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField(max_length=50)

    def __str__(self):
        return self.nome
    