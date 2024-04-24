from django import forms
from django.utils.translation import gettext_lazy as _
from .models import AnimalModel
from .models import AtendimentoModel
from .models import ClinicaModel
from .models import TutorModel

# criando um formulario para cada modelo
class AnimalForm(forms.ModelForm):
 
    # criando classe Meta
    class Meta:
        # definindo modelo a ser usado
        model = AnimalModel
 
        # definindo campos a serem usados
        fields = [
            "Anim_Nome",
            "Anim_Especie",
            "Anim_Raca",
            "Anim_Sexo",
            "Anim_Idade",
            "Anim_Peso",
            "Anim_Caracteristicas",
            "Tutor_idTutor"
        ]

        labels = {
            'Anim_Nome': _('Nome'),
            'Anim_Especie': _('Especie'),
            'Anim_Raca': _('Raça'),
            'Anim_Sexo': _('Sexo'),
            'Anim_Peso': _('Peso'),
            'Anim_Caracteristicas': _('Caracteristicas'),
            'Tutor_idTutor': _('Tutor')
        }

# criando um formulario para cada modelo
class AtendimentoForm(forms.ModelForm):
 
    # criando classe Meta
    class Meta:
        # definindo modelo a ser usado
        model = AtendimentoModel
 
        # definindo campos a serem usados
        fields = [
            "Aten_Data",
            "Aten_Obs",
            "Animal_idAnimal",
            "Animal_Tutor_idTutor",
            "Clinica_idClinica"
        ]

        labels = {
            'Aten_Data': _('Data'),
            'Aten_Obs': _('observações'),
            'Animal_idAnimal': _('Animal'),
            'Animal_Tutor_idTutor': _('Tutor'),
            'Clinica_idClinica': _('Clinica')
        }

# criando um formulario para cada modelo
class ClinicaForm(forms.ModelForm):
 
    # criando classe Meta
    class Meta:
        # definindo modelo a ser usado
        model = ClinicaModel
 
        # definindo campos a serem usados
        fields = [
            "Clin_Estabelecimento",
            "Clin_Endereco",
            "Clin_Bairro",
            "Clin_Telefone",
            "Clin_Veterinario",
            "Clin_CRM"
        ]

        labels = {
            'Clin_Estabelecimento': _('Estabelecimento'),
            'Clin_Endereco': _('Endereco'),
            'Clin_Bairro': _('Bairro'),
            'Clin_Telefone': _('Telefone'),
            'Clin_Veterinario': _('Veterinario'),
            'Clin_CRM': _('CRM')
        }

# criando um formulario para cada modelo
class TutorForm(forms.ModelForm):
 
    # criando classe Meta
    class Meta:
        # definindo modelo a ser usado
        model = TutorModel
 
        # definindo campos a serem usados
        fields = [
            "Tut_Nome",
            "Tut_Endereco",
            "Tut_Bairro",
            "Tut_Fone",
            "Tut_CPF",
            "Tut_RG",
            "Tut_Ong"
        ]

        labels = {
            'Tut_Nome': _('Nome'),
            'Tut_Endereco': _('Endereco'),
            'Tut_Bairro': _('Bairro'),
            'Tut_Fone': _('Telefone'),
            'Tut_CPF': _('CPF'),
            'Tut_RG': _('RG'),
            'Tut_Ong': _('Ong')
        }