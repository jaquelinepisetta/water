
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import waterform                   ########################## importa o formulario  Dogform definido no arquivo forms
from app1.models import water               ######################### importa o modelo de dados Dogs  definido no arquivo models
from django.contrib.gis.geos import GEOSGeometry  ######################### importa a funçao geosgeometry que codifica diversos formatos em tipo geometry (postgis)
import json
from django.contrib.gis.geos import Point


# Create your views here.

def site(request):
    return render(request, 'app1/index.html')
def apresenta(request):
    img = water.objects.all() #########################  requisita todos as linhas da tabela dogs do banco de dados
    return render(request, 'app1/apresenta.html',{'img': img} ) ######################### retorna a pagina apresenta.html e passa como parametros todas as linhas da tabela dogs do banco de dados


def site(request):

    form = waterform ######################### cria uma nova instancia do formulario dogform
    return render(request, 'app1/main.html',{'form': form} ) ######################### retorna a pagina main.html e passa como parametro o formulario waterform

# def split(string, sep):
#     """Return the string split by sep.
#
#     Example usage: {{ value|split:"/" }}
#     """
#     return string.split(sep)

def add_water(request):

    if request.method == 'POST': ######################## verifica se a requisição utiliza o método http POST
        form = waterform(request.POST, request.FILES) ######################## cria uma instancia do formulário dogform com as informações passadas pelo no request que veio das paginas html,
        p = request.POST['geojson'] ######################## pega a coordenada em geojson que é inserida na pagina web no input do "Form html"
        print p
        # data = json.loads(p) ######################## decodifica o geojson e transforma em um dicionário
        # p=data['geometry'] ######################## pega a parte de geometria do geojson necessario para codificar utilizando a biblioteca GEOS
        # p = json.dumps(p) ######################## codifica p como geojson
        # print p['lat']
        lat=p.split(',')[0].split(':')[1]
        lng=p.split(',')[1].split(':')[1].replace("}", "")
        print lng

        point= 'POINT(%s %s)' % (lat, lng)
        # point = Point(float(lat), float(lng))
        # point = Point(-25 -49)
        point = GEOSGeometry(point) ########################codifica o geojson como geometry para inserir no banco
        # form.ponto = point

        updated_data = request.POST.copy() ######################## faço uma cópia das informações passadas no request
        updated_data.update({'ponto': point})  ######################## modifico a cópia do request trocando formato  do ponto de geojson para geometry
        form = waterform(updated_data, request.FILES) ######################## instancio o formulario com as informações modificadas e com os arquivos upados

        if form.is_valid():  ######################## verifico se o formulario instaciado é valido
            form.save() ######################## salvo o formulario no banco

        else:
            print form.errors ######################## se ocorrer algum erro é printado

        return render(request, 'app1/main.html', {'form': form})
