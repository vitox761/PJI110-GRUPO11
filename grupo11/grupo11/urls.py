"""
URL configuration for grupo11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.homePageView),
    path('admin/', views.adminPageView, name='admin'),
    path('root/', admin.site.urls),
    path('cadastro/animal',views.cadastroAnimalView, name='criar_animal'),
    path('cadastro/atendimento',views.cadastroAtendimentoView, name='criar_atendimento'),
    path('cadastro/clinica',views.cadastroClinicaView, name='criar_clinica'),
    path('cadastro/tutor',views.cadastroTutorView, name='criar_tutor'),
    path('visualizar/animal',views.visualizarAnimalView,name='visualizar_animal'),
    path('visualizar/atendimento',views.visualizarAtendimentoView,name='visualizar_atendimento'),
    path('visualizar/clinica',views.visualizarClinicaView,name='visualizar_clinica'),
    path('visualizar/tutor',views.visualizarTutorView,name='visualizar_tutor'),
    path('editar/animal/<id>',views.editarAnimalView, name='editar_animal'),
    path('editar/atendimento/<id>',views.editarAtendimentoView, name='editar_atendimento'),
    path('editar/clinica/<id>',views.editarClinicaView, name='editar_clinica'),
    path('editar/tutor/<id>',views.editarTutorView, name='editar_tutor'),
    path('deletar/animal/<id>',views.deletarAnimalView, name='deletar_animal'),
    path('deletar/atendimento/<id>',views.deletarAtendimentoView, name='deletar_atendimento'),
    path('deletar/clinica/<id>',views.deletarClinicaView, name='deletar_clinica'),
    path('deletar/tutor/<id>',views.deletarTutorView, name='deletar_tutor'),
    path('favicon.ico', RedirectView.as_view(url='/static/images/pet-icon.ico'))
]
