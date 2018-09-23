from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Fornecedor(models.Model):
    nome_completo = models.CharField('Nome completo', max_length=100)
    email = models.EmailField('Email', max_length=70)
    telefone = models.CharField('Telefone', max_length=10)
    endereco = models.CharField('Endereço', max_length=100)
    cidade = models.CharField('Cidade', max_length=30)
    residuos = models.CharField('Resíduos', max_length=100)
    tipo_residuos = models.CharField('Tipo de Resíduos', max_length=100)
    volume_produto = models.CharField('Volume de Resíduos', max_length=30)   
    image = models.ImageField('Imagem Resíduo', upload_to='foto_residuo')
    date = models.DateTimeField(default = timezone.now)
    
    def __str__(self):
        return str(self.nome_completo)

class Empresa(models.Model):
    nome_empresa = models.CharField('Nome da Empresa', max_length=100)
    cnpj = models.CharField('CNPJ',max_length=50)
    endereco = models.CharField('Endereço', max_length=100)
    email = models.EmailField('Email Endereço', max_length=50)
    telefone = models.CharField('Telefone', max_length=13)

    def __str__(self):
        return str(self.nome_empresa)

class Interesse(models.Model):
    nome_empresa = models.CharField('Empresa', max_length=100)
    email = models.EmailField('Email Endereço', max_length=50)
    fornecedor = models.ForeignKey('Fornecedor',on_delete=models.PROTECT)

    def __str__(self):
        return str(self.nome_empresa) + ' com interesse em resíduos ' + str(self.fornecedor.residuos) + ' Fornecido por ' + str(self.fornecedor)

class Apoiadores(models.Model):
    nome = models.CharField('Nome Apoiador', max_length=100)    
    funcao = models.CharField('Função', max_length=200)
    descricao = models.TextField('Descrição', max_length=500)
    image = models.ImageField('Imagem Destaque', upload_to = 'logo-apoiadores')
    date = models.DateTimeField('Data registro', default = timezone.now)

    def __str__(self):
        return str(self.nome)
    
class Newsletter(models.Model):
    email = models.EmailField('Email', max_length=50)

    def __str__(self):
        return str(self.email)
