from django.urls import path
from modpry.app_regpry.views import *
from modpry.app_modpry.views import *
from modpry.app_regpry.funciones import *
from .models import *


urlpatterns = [ 
    #URL para registro de un proyecto
    path('inicio',vst_pry().vst_inicio, name = 'inicio_pry'), #inicio de la app de proyectos
    path('creapry/',vts_reg_pry.as_view(), name = 'crea_pry'), #Crea el proyecto 
    path('cnpry/', vst_ls_pry.as_view(), name='cn_pry'), #Lista de proyectos
    path('editpry/<int:pk>/',vts_edit_pry.as_view(), name = 'edit_pry'), #Actualizar proyecto
    path('archipry/<id>',archi_pry, name = 'archi_pry'), #Archivar un proyecto
    path('elipry/<id>',eli_pry, name = 'eli_pry'),#Eliminar un proyecto
]