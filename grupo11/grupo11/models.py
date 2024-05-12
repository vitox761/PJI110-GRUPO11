from django.db import models
from django.utils.translation import gettext_lazy as _

# declarar modelo "ClinicaModel"
class ClinicaModel(models.Model):
 
    # campos do modelo
    Clin_Estabelecimento = models.CharField(max_length = 45)
    Clin_Endereco = models.CharField(max_length = 200)
    Clin_Bairro = models.CharField(max_length = 45)
    Clin_Telefone = models.CharField(max_length = 20)
    Clin_Veterinario = models.CharField(max_length = 45)
    Clin_CRM = models.CharField(max_length = 45)

    def __str__(self):
        return self.Clin_Estabelecimento

# declarar modelo "TutorModel"
class TutorModel(models.Model):
    
    class Ong(models.IntegerChoices):
        NAO = (0, _('Não'))
        SIM = (1, _('Sim'))

    # campos do modelo
    Tut_Nome = models.CharField(max_length = 200)
    Tut_Endereco = models.CharField(max_length = 200)
    Tut_Bairro = models.CharField(max_length = 45)
    Tut_Fone = models.CharField(max_length = 45)
    Tut_CPF = models.CharField(max_length = 45)
    Tut_RG = models.CharField(max_length = 45)
    Tut_Ong = models.SmallIntegerField(
        choices=Ong.choices,
        default=Ong.NAO
    )

    def __str__(self):
        return self.Tut_Nome

# declarar modelo "AnimalModel"
class AnimalModel(models.Model):
 
    class Especies(models.TextChoices):
        CAO = ("Canino", _('Canino'))
        GATO = ("Felino", _('Felino'))

    class Sexos(models.TextChoices):
        MACHO = ("Macho", _('Macho'))
        FEMEA = ("Fêmea", _('Fêmea'))

    # campos do modelo
    Anim_Nome = models.CharField(max_length = 45)
    Anim_Especie = models.CharField(max_length = 45, choices = Especies.choices, default = Especies.CAO)
    Anim_Raca = models.CharField(max_length = 45)
    Anim_Sexo = models.CharField(max_length = 45, choices = Sexos.choices, default = Sexos.MACHO)
    Anim_Idade = models.IntegerField()
    Anim_Peso = models.DecimalField(max_digits = 3, decimal_places = 2)
    Anim_Caracteristicas = models.CharField(max_length = 200, blank = True, default = '')
    Tutor_idTutor = models.ForeignKey(TutorModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.Anim_Nome

# declarar modelo "AtendimentoModel"
class AtendimentoModel(models.Model):
 
    # campos do modelo
    Aten_Data = models.DateField(blank = True, null = True)
    Aten_Obs = models.CharField(max_length = 200, blank = True, default = '')
    Animal_idAnimal = models.ForeignKey(AnimalModel, on_delete=models.CASCADE)
    Animal_Tutor_idTutor = models.ForeignKey(TutorModel, on_delete=models.CASCADE)
    Clinica_idClinica = models.ForeignKey(ClinicaModel, on_delete=models.CASCADE)



