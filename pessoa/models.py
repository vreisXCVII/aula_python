from django.db import models
from django.template.defaultfilters import default
from _datetime import datetime
from unittest.util import _MAX_LENGTH

# Create your models here.

class PessoaModel(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    
    cliente_nome = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Nome")
    
    endereco = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Endereco")
    

    cliente_cpf = models.CharField(
        max_length=11,
        null=False,
        blank=False,
        verbose_name="CPF")
    
    cliente_rg = models.CharField(
        max_length=9,
        default=0,
        null=False,
        blank=False,
        verbose_name="RG")
    

    class Meta:
        ordering = ['cliente_nome']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.pessoa_nome


class ContatoModel(models.Model):
    

    venda_id = models.AutoField(primary_key=True)
                      
    
    cliente = models.ForeignKey(PessoaModel, on_delete=models.CASCADE)
    
    venda_data = models.DateField(
                     null=False, 
                     default=datetime(2019, 7, 20, 15, 30, 4, 971732),
                     verbose_name="Data Venda")
    
    valor_total_venda = models.FloatField(
        max_length = 20,
        null = True,
        blank = False,
        verbose_name = 'Valor total')
    
    
    class Meta:
        ordering = ['venda_id']
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'

    def __str__(self):
        return self.venda_id
    
                    

