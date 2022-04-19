from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

from modadm.App_modadm.models import usu


class frm_reg_usu_su(forms.ModelForm):
    #Calse que automatiza la creación de formularios de Registro de Super Usuario en Django.
    class Meta:
        model = usu
        fields = '__all__'

class frm_reg_usu_adm(forms.ModelForm):
    #Calse que automatiza la creación de formularios de Registro de Usuario en Django.
    class Meta:
        model = usu
        fields = ['username',
                  'password',
                  'first_name',
                  'last_name',
                  'email',
                  'is_staff',
                  'is_active'
                 ]
class frm_reg_usu(UserCreationForm):
    #Calse que automatiza la creación de formularios de Registro de Usuario en Django.
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = usu
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

