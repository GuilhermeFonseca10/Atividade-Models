
from django.db import models
from usuario.models.categoria import Categoria

from usuario.models.locacao import Locacao

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.DateField()
    valor_locacao = models.IntegerField()
    
    locacao = models.ManyToManyField(Locacao)
    filme = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.titulo)
        