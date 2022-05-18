from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import UpdateView,FormView, CreateView, ListView
from django.urls import reverse_lazy
from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
#from rest_framework import viewsets

from .models import *
from modpry.App_regpry.models import *
from modpry.App_regpry.form import *

class vst_pry():
    #Clase que procesa las vistas del IU del registro de proyectos de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_pry_iu.html")

#--------------------------- Registro de proyecto individual ---------------------------------
class vts_reg_pry(CreateView):
    #Clase de la vista de registro de proyecto 
    model = pry_base
    form_class = frm_reg_pry
    template_name = 'iu_pub/serv_iu/App_regpry_frm_crearpry.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un proyecto' 
        context ['action'] = 'add'
        return context

class vts_ls_pry(ListView):
    # clase para listar proyectos del sistema
    model = pry_base
    template_name = 'cn_pry.html'
    queryset = pry_base.objects.order_by('nombre_pry')
    context_object_name = 'lista_pry'
    #success_url = reverse_lazy('cn_pry.html')
    #success_message = 'listado cargado correctamente'

    def get_context_data(self, **kwargs):
        context = super(vts_ls_pry, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Listado de proyectos'
        return context

class vts_edit_pry(UpdateView):
    #Clase de la vista para actualizar el registro de un proyecto 
    model = pry_base
    form_class = frm_reg_pry
    template_name = 'iu_pub/serv_iu/App_regpry_frm_editpry.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un proyecto' 
        context ['entity'] = 'pry'
        context ['list_url'] = reverse_lazy('cn_pry')
        context ['action'] = 'edit'
        return context

#---------------------------Se elimina el proyecto de la base datos tambien-----------------------------
#class vts_reg_pry(DeleteView):
    #Clase de la vista para borrar el registro de proyecto 
#    model = proyecto
#    success_url = reverse_lazy('') #Retornar a la pagina de consultar proyecto

def eli_pry(request,id):
    pry = pry_base.objects.get(id_pry=id)
    if request.method == 'POST':
        pry.delete()
        return redirect('cn_pry')
    return render (request, 'pry/app_pry/App_regpry_frm_elimpry.html',{'pry_base': pry_base})

#--------------------------- Registro de proyecto grupal ---------------------------------

class vts_reg_pry_grp(CreateView):
    #Clase de la vista de registro de proyecto 
    model = pry_grp
    form_class = frm_reg_pry_grp
    template_name = 'iu_pub/serv_iu/App_regpry_frm_crearpry.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un proyecto grupal' 
        context ['action'] = 'add'
        return context
#--------------------------- Registro de proyecto  ---------------------------------------
#--------------------------- Registro de proyecto individual -----------------------------