from django.shortcuts import render

from .models import ClinicaModel
from .forms import ClinicaForm
from .models import AnimalModel
from .forms import AnimalForm
from .models import TutorModel
from .forms import TutorForm
from .models import AtendimentoModel
from .forms import AtendimentoForm

def homePageView(request):
    context ={}
         
    return render(request, "homepage.html")

def adminPageView(request):
    context ={}
         
    return render(request, "admin.html")

def cadastroClinicaView(request):
    context ={}

    form = ClinicaForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
         
    context['form']= form
    if request.method == 'POST':
        return render(request,'clinica_sucesso.html',context)
    else:
        return render(request, "clinica_cadastro.html", context)

def cadastroAnimalView(request):
    context ={}
 
    form = AnimalForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
         
    context['form']= form
    if request.method == 'POST':
        return render(request,'animal_sucesso.html',context)
    else:
        return render(request, "animal_cadastro.html", context)

def cadastroAtendimentoView(request):
    context ={}
 
    form = AtendimentoForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print(form.errors) 

    context['form']= form
    if request.method == 'POST':
        return render(request,'atendimento_sucesso.html',context)
    else:
        return render(request, "atendimento_cadastro.html", context)

def cadastroTutorView(request):
    context ={}
 
    form = TutorForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
         
    context['form']= form
    if request.method == 'POST':
        return render(request,'tutor_sucesso.html',context)
    else:
        return render(request, "tutor_cadastro.html", context)

def visualizarClinicaView(request):

	form_item = ClinicaForm()
	clinicas = ClinicaModel.objects.all()  

	return render(request, 'clinica_visualizar.html', 
		{
		'form_item': form_item,
		'clinicas': clinicas
		})

def visualizarTutorView(request):

	form_item = TutorForm()
	tutores = TutorModel.objects.all()  

	return render(request, 'tutor_visualizar.html', 
		{
		'form_item': form_item,
		'tutores': tutores
		})

def visualizarAnimalView(request):

	form_item = AnimalForm()
	animais = AnimalModel.objects.all()  

	return render(request, 'animal_visualizar.html', 
		{
		'form_item': form_item,
		'animais': animais
		})

def visualizarAtendimentoView(request):

	form_item = AtendimentoForm()
	atendimentos = AtendimentoModel.objects.all()  

	return render(request, 'atendimento_visualizar.html', 
		{
		'form_item': form_item,
		'atendimentos': atendimentos
		})

def editarClinicaView(request,id):
    instance = ClinicaModel.objects.get(id=id)
    form = ClinicaForm(instance=instance)
    context = {'form': form, 'instance': instance}

    if request.method == 'POST':
        form = ClinicaForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return render(request,'clinica_sucesso_editar.html',context)
    else:
        return render(request, 'clinica_editar.html', context)

def editarAnimalView(request,id):
    instance = AnimalModel.objects.get(id=id)
    form = AnimalForm(instance=instance)
    context = {'form': form, 'instance': instance}

    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return render(request,'animal_sucesso_editar.html',context)
    else:
        return render(request, 'animal_editar.html', context)

def editarAtendimentoView(request,id):
    instance = AtendimentoModel.objects.get(id=id)
    form = AtendimentoForm(instance=instance)
    context = {'form': form, 'instance': instance}

    if request.method == 'POST':
        form = AtendimentoForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return render(request,'atendimento_sucesso_editar.html',context)
    else:
        return render(request, 'atendimento_editar.html', context)

def editarTutorView(request,id):
    instance = TutorModel.objects.get(id=id)
    form = TutorForm(instance=instance)
    context = {'form': form, 'instance': instance}

    if request.method == 'POST':
        form = TutorForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return render(request,'tutor_sucesso_editar.html',context)
    else:
        return render(request, 'tutor_editar.html', context)


def deletarClinicaView(request,id):
    instance = ClinicaModel.objects.get(id=id)
    form = ClinicaForm(instance=instance)
    context = {'form': form, 'instance': instance}
    ClinicaModel.objects.filter(id=id).delete()

    return render(request, 'clinica_deletar.html',context)

def deletarAnimalView(request,id):
    instance = AnimalModel.objects.get(id=id)
    form = AnimalForm(instance=instance)
    context = {'form': form, 'instance': instance}
    AnimalModel.objects.filter(id=id).delete()

    return render(request, 'animal_deletar.html',context)

def deletarAtendimentoView(request,id):
    instance = AtendimentoModel.objects.get(id=id)
    form = AtendimentoForm(instance=instance)
    context = {'form': form, 'instance': instance}
    AtendimentoModel.objects.filter(id=id).delete()

    return render(request, 'atendimento_deletar.html',context)

def deletarTutorView(request,id):
    instance = TutorModel.objects.get(id=id)
    form = TutorForm(instance=instance)
    context = {'form': form, 'instance': instance}
    TutorModel.objects.filter(id=id).delete()

    return render(request, 'tutor_deletar.html',context)