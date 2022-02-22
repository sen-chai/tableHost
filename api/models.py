from enum import unique
from django.db import models

class ClienteOmie(models.Model):
    cod_cliente = models.CharField(max_length=15,null=False)
    nome_fantasia = models.CharField(max_length=60)
    razao_social = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=60)
    logradouro = models.CharField(max_length=60)

class VendedorOmie(models.Model):
    cod_vendedor = models.CharField(max_length=15)
    nome_vendedor = models.CharField(max_length=20)

class ProdutoOmie(models.Model):
    cod_produto = models.CharField(max_length=30)
    codigo_produto = models.CharField(max_length=40)
    nome_produto = models.CharField(max_length=120)

class PedidoPendencia(models.Model):
    cod_pedido = models.IntegerField(null=False,unique=True)
    #* agenda
    AGENDA_STATUS=[
        ('AGENDADO','AGENDADO'),
        ('AGUARDANDO CONFIRMACAO DO CLIENTE','AGUARDANDO CONFIRMACAO DO CLIENTE'),
        ('NAO PRODUZIR','NAO PRODUZIR')
    ]
    status_agenda = models.CharField(max_length=30)
    data_agenda = models.DateField()
    data_liberado = models.DateField()
    liberado_por = models.CharField(max_length=30)
    data_expedicao = models.DateField()
    status_expedicao = models.CharField(max_length=30)
    #* expedicao
    EXPEDICAO_STATUS = [ ]

class ItemPendencia(models.Model):
    cod_pedido = models.IntegerField(null=False,unique=True)
    #* pendencias
    PENDENCIA_STATUS = [
        ('A CONSOLIDAR','A CONSOLIDAR'),
        ('CONSOLIDADO','CONSOLIDADO'),
        ('FALTA DE MATERIAL','FALTA DE MATERIAL'),
    ]
    status_pedencia = models.CharField(max_length=30)

    #todo relatorio de expedicao eh pedido ou item?
    # todo n'ao esta na hora de otimizar pedidos solicitados, simplifique o maximo possivel
