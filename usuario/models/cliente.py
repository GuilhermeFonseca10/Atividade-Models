from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nome)
