# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-04 03:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corebib', '0002_auto_20171204_0334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='matricula',
            new_name='cod',
        ),
        migrations.RenameField(
            model_name='editora',
            old_name='cod_e',
            new_name='cod',
        ),
    ]