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
    #emprestimos = models.ManyToOneRel('Aluno')
    #disponibilidade ? se emprestado=0 , se livre=1

    def __str__(self):
        return unicode(self.titulo)
    
class Aluno(models.Model):
    matricula = models.IntegerField()
    nome = models.CharField(max_length=30)
    #multa = models.FloatField()
    #emprestimos = models.ManyToManyField(Livro)

    def __str__(self):
        return unicode(self.nome)

'''        
class Emprestimo(models.Model):
    id_aluno = models.ForeignKey(Aluno)
    id_livro = models.ForeignKey(Livro)
    #data = models.CharField(date)
    #devolucao = models.CharField(date)
 '''