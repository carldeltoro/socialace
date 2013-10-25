#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from appproyecto.models import usuario
from django.forms.extras.widgets import SelectDateWidget

CHOICES = (('1', 'Privado',), ('2', 'Publico',))

class registroForm(ModelForm):
	usu_nombreUsuario = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Nombre Usuario', 'class':'inputbox name'}))
        usu_clave = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Password', 'class':'inputbox password'}))
        usu_nombre = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Nombre', 'class':'inputbox name'}))
        usu_apellido = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Apellido', 'class':'inputbox name'}))
        usu_correo = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Correo Electronico', 'class':'inputbox email'}))
        usu_direccion = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Ubicacion Actual', 'class':'inputbox name'}))
        usu_twitter = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'twitter', 'class':'inputbox twitter'}))
        usu_facebook = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'facebook', 'class':'inputbox facebook'}))
        usu_google = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'google +', 'class':'inputbox googleplus'}))
        usu_fechanacimiento = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Fecha Nacimiento', 'class':'inputbox name','id':'datepicker'}))
        usu_privacidad = forms.ChoiceField(label='Privacidad',widget=forms.RadioSelect, choices=CHOICES)

        #usu_privacidad = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'privacidad', 'class':'inputbox name'}))
	class Meta:
		model = usuario
		
		
class LoginForm(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'usuario', 'class':'input-normal required usuario'}),label='usuario')
	password = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'password', 'class':'input-normal required password'}),label='password')

