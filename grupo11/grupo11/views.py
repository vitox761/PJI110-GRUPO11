from django.shortcuts import render

from .models import ClinicaModel
from .forms import ClinicaForm
 
 
def createClinicaView(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ClinicaForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "clinica_view.html", context)

def displayClinicaView(request):

	form_item = ClinicaForm()

	# grab all Clinicas from database:
	all_clinicas = ClinicaModel.objects.all()  

	return render(request, 'display_clinica.html', 
		{
		'form_item': form_item,
		'all_clinicas': all_clinicas
		})