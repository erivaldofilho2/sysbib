# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from datetime import date

# Create your models here.

class Editora(models.Model):
    cod = models.IntegerField()
    nome = models.CharField(max_length=30)
    def __str__(self):
        return unicode(self.nome)

class Autor(models.Model):
    cod = models.IntegerField()
    nome = models.CharField(max_length=30)
    def __str__(self):
        return unicode(self.nome)
    
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    volume = models.IntegerField()
    autor = models.ForeignKey(Autor)
    editora = models.ForeignKey(Editora)

    def __str__(self):
        return unicode(self.titulo)

    
class Aluno(models.Model):
    matricula = models.IntegerField()
    nome = models.CharField(max_length=30)
    def __str__(self):
        return unicode(self.nome)

class Emprestimo(models.Model):
    livro = models.OneToOneField(Livro)
    aluno = models.ForeignKey(Aluno)
    data = models.DateField()

    def __str__(self):
        return unicode('Aluno: '+self.aluno.nome+'/ Livro: '+self.livro.titulo+'/ Entrar em: ')