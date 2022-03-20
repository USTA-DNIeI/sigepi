from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
#from rest_framework.routers import DefaultRouter
from modadm.App_modadm.views import *



urlpatterns = [

# direcciones del modulo admin
    path('inicioadmin', backend.modadm, name="inicioadmin"),

# registrar modulos
    path('vts_reg_modu', vts_reg_mod.as_view(), name ='reg_mod'),
    path('vts_ls_modu', vts_ls_mod.as_view(), name ='reg_mod'),
    path('vts_edt_modu', vts_edt_mod.as_view(), name ='reg_mod'),
    path('vts_eli_modu', vts_eli_mod, name ='reg_mod'),

#funciones
    path('funciones/',funcionList.as_view(), name = 'funciones'),
    path('crearfun/',funcionCreate.as_view(), name = 'crearfun'),
    path('editarfun/<int:pk>/',funcionUpdate.as_view(), name='editarfun'),
    path('eliminarfun/<int:pk>/',funcionDelete.as_view(), name='eliminarfun')

]
