from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    rua = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    
    def __str__(self): 
        return self.nome