from tokenize import group
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .models import *

class funcionForm(forms.ModelForm):
    class Meta:
        model =  func_app
        fields = '__all__'

class frm_reg_mod(forms.ModelForm):
    #Calse que automatiza la creación de formularios de Registro de Usuario en Django.
    class Meta:
        model =  mod
        fields = '__all__'

class frm_con_mod(forms.ModelForm):
    #Clase que automatiza la creación de formularios de consulta de Usuario en Django.
    class Meta:
        model =  mod
        fields = '__all__'

class frm_reg_app_mod(forms.ModelForm):
    class Meta:
        model =  app_mod
        fields = '__all__'

class frm_con_app_mod(forms.ModelForm):
    class Meta:
        model =  app_mod
        fields = '__all__'

class frm_con_group(forms.ModelForm):
    class Meta:
        model =  Group
        fields = '__all__'

class frm_con_rol(forms.ModelForm):
    class Meta:
        model =  rol
        fields = '__all__'