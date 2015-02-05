from django.db import models


class RotaCiclismo(models.Model):
    id_rota = models.AutoField(primary_key=True)
    nome_rota = models.CharField(max_length=200)
    descricao_rota = models.CharField(max_length=1024)
    tipo_rota = models.CharField(max_length=1024)


class Coordenadas(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    idcoord = models.AutoField(primary_key=True)


class RotaPonto (models.Model):
    coordenada_id = models.ForeignKey(Coordenadas)
    rota_id = models.ForeignKey(RotaCiclismo)


class PontoTuristico(models.Model):
    id_ponto = models.AutoField(primary_key=True)
    nome_ponto = models.CharField(max_length=1024)
    descricao_ponto = models.CharField(max_length=1024)
    coordid = models.ForeignKey(Coordenadas)