from django.contrib import admin
from .models import Filme, Locacao, Cliente, Categoria

# Register your models here.
@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'valor')

@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
