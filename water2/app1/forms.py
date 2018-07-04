# -*- coding: utf-8 -*-
from django.db import models ######################## importa a classe model do django
from django.forms import ModelForm ######################## importa a classe modelform do django (para criar formularios direto dos modelos de dados)
from app1.models import water ######################## importa a classe water do modelo de dados

######################## cria o formulário para inserir dados dos cachorros
class waterform(ModelForm):
    class Meta:
        model = water ######################## instancia a classe water
        fields = ('nome','descricao', 'problema','ponto',) ######################## define quais campos do nosso modelo de dados vai compor o formulario

class Apresentform(ModelForm):
    class Meta:
        model = water
        fields = ('nome','descricao', 'problema','ponto',)
