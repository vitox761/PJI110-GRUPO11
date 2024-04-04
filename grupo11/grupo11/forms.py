from django import forms
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
            "Clin_Veterinario",
            "Clin_CRM"
        ]

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