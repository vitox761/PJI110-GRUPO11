from django.db import models

# declarar modelo "ClinicaModel"
class ClinicaModel(models.Model):
 
    # campos do modelo
    Clin_Estabelecimento = models.CharField(max_length = 45)
    Clin_Endereco = models.CharField(max_length = 200)
    Clin_Bairro = models.CharField(max_length = 45)
    Clin_Veterinario = models.CharField(max_length = 45)
    Clin_CRM = models.CharField(max_length = 45)

# declarar modelo "TutorModel"
class TutorModel(models.Model):
 
    # campos do modelo
    Tut_Nome = models.CharField(max_length = 200)
    Tut_Endereco = models.CharField(max_length = 200)
    Tut_Bairro = models.CharField(max_length = 45)
    Tut_Fone = models.CharField(max_length = 45)
    Tut_CPF = models.CharField(max_length = 45)
    Tut_RG = models.CharField(max_length = 45)
    Tut_Ong = models.SmallIntegerField()

# declarar modelo "AnimalModel"
class AnimalModel(models.Model):
 
    # campos do modelo
    Anim_Nome = models.CharField(max_length = 45)
    Anim_Especie = models.CharField(max_length = 45)
    Anim_Raca = models.CharField(max_length = 45)
    Anim_Sexo = models.CharField(max_length = 45)
    Anim_Idade = models.IntegerField()
    Anim_Peso = models.DecimalField(max_digits = 3, decimal_places = 2)
    Anim_Caracteristicas = models.CharField(max_length = 200)
    Tutor_idTutor = models.ForeignKey(TutorModel, on_delete=models.CASCADE)

# declarar modelo "AtendimentoModel"
class AtendimentoModel(models.Model):
 
    # campos do modelo
    Aten_Data = models.DateField()
    Aten_Obs = models.CharField(max_length = 200)
    Animal_idAnimal = models.IntegerField()
    Animal_Tutor_idTutor = models.ForeignKey(TutorModel, on_delete=models.CASCADE)
    Clinica_idClinica = models.ForeignKey(ClinicaModel, on_delete=models.CASCADE)



