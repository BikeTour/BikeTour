# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordenadas',
            fields=[
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('idcoord', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id_ponto', models.AutoField(serialize=False, primary_key=True)),
                ('nome_ponto', models.CharField(max_length=1024)),
                ('descricao_ponto', models.CharField(max_length=1024)),
                ('coordid', models.ForeignKey(to='cicloponto.Coordenadas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RotaCiclismo',
            fields=[
                ('id_rota', models.AutoField(serialize=False, primary_key=True)),
                ('nome_rota', models.CharField(max_length=200)),
                ('descricao_rota', models.CharField(max_length=1024)),
                ('tipo_rota', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RotaPonto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coordenada_id', models.ForeignKey(to='cicloponto.Coordenadas')),
                ('rota_id', models.ForeignKey(to='cicloponto.RotaCiclismo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
