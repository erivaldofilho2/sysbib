# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from corebib.models import *

# Register your models here.
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Aluno)
admin.site.register(Emprestimo)