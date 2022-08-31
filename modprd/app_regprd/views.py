# App de registro de producto - Vistas para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 19 -08 -2022

from django.shortcuts import render
from django.http import HttpResponse
from modprd.app_regprd.form import *
from django.urls import reverse_lazy
from modprd.app_regprd.models import *
from .models import *
from django.views.generic import *

#Vista principal del registro de productos 

class ini_regprd():
    def view_prd(request):
        return render(request, 'app_regprd_iu.html')

#Vista para el registro de producto

class vst_regprd(CreateView):
    model= prd_base
    form_class = form_reg_prd
    template_name ='mod_prd_frm_registrar.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_base.objects.filter(id_usu =self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'registrar un producto'
        context['action'] = 'add'
        return context

#Vista para el registro de un requerimiento de existencia

class vst_regreqexist(CreateView):
    model= prd_req_Exist
    form_class = form_req_exist
    template_name ='mod_prd_frm_requexist.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_Exist.objects.filter(nom_reqexs =self.request.user)

#Vista para el registro de un requerimiento de calidad

class vst_regreqcal(CreateView):
    model= prd_req_cal
    form_class = form_req_cal
    template_name ='mod_prd_frm_reqcal.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_cal.objects.filter(id_categ =self.request.user)

class vst_regreqcal(CreateView):
    model= prd_req_cal
    form_class = form_req_cal
    template_name ='mod_prd_frm_reqcal.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_cal.objects.filter(id_categ =self.request.user)

class vst_regcateg(CreateView):
    model= prd_categ
    form_class = form_categ
    template_name ='mod_prd_frm_categ.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_cal.objects.filter(id_categ =self.request.user)

class vst_regtipo(CreateView):
    model= prd_tipo
    form_class = form_tipo
    template_name ='mod_prd_frm_tipo.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_cal.objects.filter(id_categ =self.request.user)

class vst_regcampo(CreateView):
    model= campo
    form_class = form_campo
    template_name ='mod_prd_frm_campo.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_cal.objects.filter(id_categ =self.request.user)


