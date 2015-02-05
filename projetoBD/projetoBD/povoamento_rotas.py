# -*- encoding: utf-8 -*-

import codecs
import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetoBD.settings")
django.setup()

from cicloponto.models import RotaCiclismo, PontoTuristico, Coordenadas, RotaPonto


if __name__ == '__main__':
	c = 0

	with open('C:\\Users\\Mariana Melo\\Desktop\\projetoBD\\ponto.json', 'r') as arq_pontos:
		pontos = json.load(arq_pontos)

		for ponto in pontos['features']:
			ponto_coord = Coordenadas.objects.get_or_create(latitude=ponto['geometry']['coordinates'][1], longitude=ponto['geometry']['coordinates'][0])
			ponto = PontoTuristico.objects.get_or_create(nome_ponto=ponto['properties']['PTurist'], descricao_ponto=ponto['properties']['Descritv'], 
				                                         coordid=ponto_coord[0])

			print c
			c += 1
	c = 0
	with open('C:\\Users\\Mariana Melo\\Desktop\\projetoBD\\rota.json', 'r') as arq_rotas:
		rotas = json.load(arq_rotas)

		for rota in rotas['features']:
			rota_cicl = RotaCiclismo.objects.get_or_create(nome_rota=rota['properties']['Name'], descricao_rota=rota['properties']['Description'], tipo_rota=rota['properties']['Type'])

			for coordenada in rota['geometry']['coordinates']:
				rota_coord = Coordenadas.objects.get_or_create(latitude=coordenada[1], longitude=coordenada[0])
				rota_ponto = RotaPonto.objects.get_or_create(coordenada_id=rota_coord[0], rota_id=rota_cicl[0])

			print c
			c += 1
