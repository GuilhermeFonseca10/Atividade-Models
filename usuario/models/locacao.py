
from usuario.models.cliente import Cliente
from django.db import models

class Locacao(models.Model):
    data_entrega = models.DateField()
    data_locacao = models.DateField()
    valor = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.data_locacao)
        