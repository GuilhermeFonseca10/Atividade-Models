from django.contrib import admin
from usuario.models.categoria import Categoria
from usuario.models.cliente import Cliente
from usuario.models.filme import Filme
from usuario.models.locacao import Locacao

admin.site.register(Cliente)
admin.site.register(Locacao)
admin.site.register(Filme)
admin.site.register(Categoria)



# Register your models he
