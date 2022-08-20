#app del registro de un producto-Modelos para SIGEPI
#AUTOR Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 12-08-2022

from django.db import models
from unittest.util import _MAX_LENGTH
from modadm.app_modadm.models import *
from modadm.app_modadm.dic import *
from django.core.validators import MaxValueValidator, MinValueValidator
from modprd.app_certprd.models import *
from modpry.app_regpry.models import *



DIC_APP = [
    #Diccionario de la aplicacion

    ['Titulo', "App Registro de Producto de Investigación"],
    ['Descripción',"Aplicación para la definición del registro del Producto de Investigación"],
    ['url_documento','doc'],
    ['url_install','modprd/app_regprd'],
    #['url_plantilla','app_regprd_iu.html'],
    #['Nombre_url','ini_regprd'],
    ['Versión aplicación','0.0.0'],
    ['id_mod', 5],
    ['Versión_módulo', 'alfa'],
    ['estado', 'en Desarrollo'],
    ['instalada', False],
    ['visible', False],
]
# Diccionario de los roles de la aplicacion
ROL_APP = [
    (0,'Investigador(a) Principal'),
    (1,'Propietario(a) Proy.'),
    (2,'Investigador(a) Secundario'),
    (3,'Colaborador(a)')
    ]

# Clases de la aplicacion de registro de productos

class prd_tipo(models.Model):
    id_tipo=models.AutoField(primary_key= True, null=False, unique=True)# Identificador del tipo del producto LLAVE PRIMARIA
    nom_tipo=models.CharField('Nombre del tipo de producto: ', max_length=255, blank=False, null=False)# Nombre del tipo de producto
    id_reqexist=models.ForeignKey(null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificadores de los requerimientos de existencia
    id_categ=models.ForeignKey(null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificador de la categoria
    id_reqcal=models.ForeignKey(null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificadores de los requerimientos de calidad
    peso_rel=models.IntegerField(null=False, blank=False, default=0)#Peso relativo de la categoria del producto
    peso_abs=models.IntegerField(null=False, blank=False, default=0)#Peso absoluto del producto segun minciencias
    vent_obs=models.IntegerField(null=False, blank=False, default=0, MaxValueValidator=10 )#ventana de observacion
    id_plt_desc=models.ForeignKey(null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    tipo_cal=models.CharField('clasificacion segun la calidad: ', max_length=10,blank=True, null=False)

class prd_req_Exist(models.Model):
    id_reqexs=models.AutoField(primary_key= True, null=False, unique=True)# Identificador del requerimiento de existencia LLAVE PRIMARIA
    nom_reqexs=models.CharField('Nombre del Requerimiento de existencia: ', max_length=255, blank=False,null=False)#Nombre del requerimiento de existencia
    desc_reqexs=models.TextField('Descripcion del Requerimiento de existencia: ', blank=True,null=False)#descripcion del requerimiento de existencia

class prd_categ(models.Model):
    id_categ=models.AutoField(primary_key= True, null=False, unique=True)# Identificador de la categoria LLAVE PRIMARIA
    nom_categ=models.CharField('Nombre de la categoria: ', max_length=255, blank=False,null=False)#Nombre de la categoria

class prd_req_cal(models.Model):
    id_reqcal=models.AutoField(primary_key= True, null=False, unique=True)# Identificador del requerimiento de calidad LLAVE PRIMARIA
    id_categ=models.ForeignKey(prd_categ, blank=False, null=False ,on_delete=models.SET_NULL, db_constraint=True)#Identificador de la categoria respectiva del requerimiento de calidad
    desc_reqcal=models.TextField('Descripcion del Requerimiento de calidad: ', blank=True,null=False)#descripcion del requerimiento de calidad

class prd_plt_desc(models.Model):
    id_plt_desc = models.AutoField(primary_key= True, null=False, unique=True)# Identificador de la plantilla de la descripcion del producto LLAVE PRIMARIA
    id_campo = models.ForeignKey(blank=False, null=False ,on_delete=models.SET_NULL, db_constraint=True)# Identificador de campo de plantilla
    nom_plt=models.CharField('Nombre de la plantilla: ', max_length=255, blank=False, null=False)#Nombre de la plantilla para el producto
    desc_plt=models.TextField('Descripcion de la plantilla: ', blank=False, null=False) #Descripcion de la plantilla de producto

class campo(models.Model):
    id_campo =  models.AutoField(primary_key= True, null=False, unique=True, unique=True)# Identificador del campo LLAVE PRIMARIA
    id_tipo_campo= models.ForeignKey(blank=False, null=False ,on_delete=models.SET_NULL, db_constraint=True) #Identificador del tipo de campo
    nom_campo=models.CharField('Nombre del campo: ', max_length=255, blank=False, null=False)#Nombre del campo
    rango = models.CharField('Rango: ', max_length=255, blank=False, null=False) #Rango del campo
    Formato = models.CharField('Formato: ', max_length=255, blank=False, null=False) #Formato del campo
    valor_def = models.IntegerField('Valor por defecto del campo:', null=False, blank=False, default=0)# Valor por defecto del campo
    desc_campo= models.TextField('descripcion del campo: ', null=False, blank=False)#descripcion del campo
    
class rl_prd (models.Model):
    id_rl =models.AutoField(primary_key=True, null=False, unique=True, blank=False, null=False ,on_delete=models.SET_NULL, db_constraint=True)# Identificador de la relacion de producto y campo LLAVE PRIMARIA
    id_Campo= models.ForeignKey("identificador del campo: ")
    valor_campo= models.IntegerField("Valor de campo: ", null=False, blank=False, default=0)#Valor de campo

class prd_base(models.Model):
    id_prd=models.AutoField(primary_key= True, null=False, unique=True)# Identificador del producto LLAVE PRIMARIA
    ids_pry=models.ForeignKey(pry_base,'Identificador del propietario: ', null=False,blank=False, ondelete=models.SET_NULL, db_constraint=True)# Identificador del propietario
    nom_prd=models.CharField('Nombre del proyecto :',max_length=255, blank=False, null=False ) # Nombre del producto
    ids_usu=models.ForeignKey(User,'Identificador del propietario: ', null=False,blank=False, ondelete=models.SET_NULL, db_constraint=True)# Identificador del propietario
    fech_reg=models.DateTimeField('Fecha de registro: ', blank=False, null=False) #fecha de registro
    fech_entrega=models.DateTimeField('Fecha de entrega: ') #fecha de entrega
    id_tipo_prd_minc=models.ForeignKey (prd_tipo,'Identificador del tipo de producto',null=True, blank=False, ondelete=models.SET_NULL, db_constraint=True) #Identificador del tipo de producto
    id_rl_prd_campos=models.ForeignKey (null=True,blank=False, ondelete=models.SET_NULL, db_constraint=True)#Identificador del campo de descripcion del producto






    

    