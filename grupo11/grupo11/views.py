from django.shortcuts import render

from .models import ClinicaModel
from .forms import ClinicaForm
 
 
def clinicaView(request):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ClinicaForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "clinica_view.html", context)