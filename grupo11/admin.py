from django.contrib import admin
from .models import AnimalModel, AtendimentoModel, ClinicaModel, TutorModel

admin.site.register(AnimalModel)
admin.site.register(AtendimentoModel)
admin.site.register(ClinicaModel)
admin.site.register(TutorModel)