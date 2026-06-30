from django.contrib import admin
from . import models

# Exibe os itens do pedido em formato de tabela dentro da página do pedido
class ItemPedidoInline(admin.TabularInline):
    model = models.ItemPedido
    extra = 1

# Associa o inline de itens ao painel de controle do pedido
class PedidoAdmin(admin.ModelAdmin):
    inlines = [
        ItemPedidoInline
    ]


admin.site.register(models.Pedido, PedidoAdmin)
admin.site.register(models.ItemPedido)
