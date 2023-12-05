from django.db import models
from datetime import date


# Dentro do modelo da padaria, terei as seguintes tabelas: user, order, payment

class atalaiashouse(models.Model):
    codClients = models.AutoField(primary_key=True, blank=False, verbose_name="ID", default="1900-01-01")

    class Usuario(models.Model):        
        nome = models.CharField(max_length=200, null=False, blank=False, verbose_name="Nome Completo")
        numero = models.IntegerField(null=False, blank=False, verbose_name='DDD Número')
        email = models.EmailField(null=False, blank=False, max_length=254, verbose_name="Email")
        cfp = models.CharField(max_length=16, null=False, blank=False, verbose_name="CPF")

        def __str__(self):
            return self.nome
        
    class Pedido(models.Model):    
        pedidoList = (
                    ("0", "Pão Francês"),
                    ("1", "Pão de Hamburguer"),
                    ("2", "Baguete de Peito de Peru"),
                    ("3", "Baguete de Frango"),
                    ("4", "Coxinha (cento)"),
                    ("5", "Kibe (cento)"),
                    ("6", "Empada de Frango (cento)"),
                    ("7", "Bolo de Festa - Chocolate"),
                    ("8", "Bolo de Festa - Morango"),
                    ("9", "Bolo de Festa - Abacaxi"),
                    ('10', "Bolo de Festa - Pelado")
                    )
        pedido = models.CharField(max_length=30, blank=False, null=False, choices=pedidoList, verbose_name="Encomendar")
        qtd = models.IntegerField(null=False, blank=False, verbose_name="Quantidade")
        dtentrega = models.DateTimeField(null=False, blank=False, verbose_name="Data de Entrega")

        def __str__(self):
            return self.pedido

    class Pagamento(models.Model):        
        pagamentoList = (
                    ("0", "Dinheiro"),
                    ("1", "Pix"),
                    ("2", "Crédito"),
                    ("3", "Dédito")
                )
        pagamento = models.CharField(max_length=15, null=False, blank=False, choices=pagamentoList, verbose_name="Forma de Pagamento")

        def __str__(self):
            return self.pagamento

    criado_em = models.DateTimeField (auto_now=True, null=False)
    atualizado_em = models.DateTimeField (auto_now=True, null=False)

    def __str__(self):
        return self.codClients


