# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class water(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao= models.CharField(max_length=50)
    problema = models.CharField(max_length=50)
    ponto = models.PointField(srid=4326)
    def __str__(self):
        return self.nome
