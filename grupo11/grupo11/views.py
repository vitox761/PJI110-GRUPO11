from django.shortcuts import render

from .models import ClinicaModel
from .forms import ClinicaForm
from .models import AnimalModel
from .forms import AnimalForm
from .models import TutorModel
from .forms import TutorForm
from .models import AtendimentoModel
from .forms import AtendimentoForm
 
def createClinicaView(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ClinicaForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    if request.method == 'POST':
        return render(request,'clinica_created.html',context)
    else:
        return render(request, "clinica_view.html", context)

def createAnimalView(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = AnimalForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    if request.method == 'POST':
        return render(request,'animal_created.html',context)
    else:
        return render(request, "animal_view.html", context)

def createAtendimentoView(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = AtendimentoForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    if request.method == 'POST':
        return render(request,'atendimento_created.html',context)
    else:
        return render(request, "atendimento_view.html", context)

def createTutorView(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = TutorForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
         
    context['form']= form
    if request.method == 'POST':
        return render(request,'tutor_created.html',context)
    else:
        return render(request, "tutor_view.html", context)

def displayClinicaView(request):

	form_item = ClinicaForm()

	# grab all Clinicas from database:
	all_clinicas = ClinicaModel.objects.all()  

	return render(request, 'display_clinica.html', 
		{
		'form_item': form_item,
		'all_clinicas': all_clinicas
		})