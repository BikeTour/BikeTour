from django.contrib import admin
from cicloponto.models import RotaCiclismo, PontoTuristico, Coordenadas, RotaPonto

# Register your models here.
admin.site.register(RotaCiclismo)
admin.site.register(Coordenadas)
admin.site.register(RotaPonto)
admin.site.register(PontoTuristico)