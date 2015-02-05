from django.shortcuts import render
from cicloponto.models import RotaCiclismo, PontoTuristico, Coordenadas, RotaPonto
from django.db import connection
import json


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def view_index(request):
	variaveis = {}
	resultados = None
	filtro = False

	cursor = connection.cursor()
	pontos = PontoTuristico.objects.all()
	coordenadas = Coordenadas.objects.filter(pontoturistico__in=pontos)

	if request.method == 'GET':

		if 'pesquisa' in request.GET or 'museu' in request.GET or 'teatro' in request.GET or 'mercado' in request.GET:

			filtro_query = "SELECT nome_ponto, descricao_ponto, latitude, longitude FROM cicloponto_pontoturistico AS pto INNER JOIN cicloponto_coordenadas AS coord ON pto.coordid_id = coord.idcoord WHERE "

			if 'pesquisa' in request.GET:
				filtro_query = "SELECT nome_ponto, descricao_ponto, latitude, longitude FROM cicloponto_pontoturistico AS pto INNER JOIN cicloponto_coordenadas AS coord ON pto.coordid_id = coord.idcoord WHERE nome_ponto LIKE '%%%s%%' " % request.GET.get('pesquisa')

			if 'museu' in request.GET:
				filtro_query = "nome_ponto LIKE '%Museu%' "

				if 'mercado' in request.GET or 'igreja' in request.GET:
					filtro_query = filtro_query + 'OR'

			if 'mercado' in request.GET:
				filtro_query = filtro_query + " nome_ponto LIKE '%Mercado%' "

				if 'igreja' in request.GET:
					filtro_query = filtro_query + 'OR'

			if 'igreja' in request.GET:
				filtro_query = filtro_query + " nome_ponto LIKE '%Igreja%' "                                                    

			print filtro_query
			cursor.execute(filtro_query + ';')
			resultados = json.dumps(dictfetchall(cursor))
			cursor.close()
			filtro = True

	variaveis['pontos'] = pontos
	variaveis['resultados'] = resultados
	variaveis['filtro'] = filtro

	return render(request, 'cicloponto/index.html', variaveis)