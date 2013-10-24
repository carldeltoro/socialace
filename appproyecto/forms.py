#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from appproyecto.models import usuario

class registroForm(ModelForm):
	usu_nombreUsuario = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Nombre Usuario', 'class':'inputbox name'}))
        usu_clave = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Password', 'class':'inputbox password'}))
        usu_nombre = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Nombre', 'class':'inputbox name'}))
        usu_apellido = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Apellido', 'class':'inputbox name'}))
        usu_correo = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Correo Electronico', 'class':'inputbox email'}))
        usu_direccion = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'Ubicacion Actual', 'class':'inputbox name'}))
        usu_twitter = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'twitter', 'class':'inputbox email'}))
        usu_facebook = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'facebook', 'class':'inputbox email'}))
        usu_google = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'google +', 'class':'inputbox email'}))
        usu_privacidad = forms.CharField(label='', max_length=20,widget=forms.TextInput(attrs={'placeholder':'privacidad', 'class':'inputbox name'}))
 
 
	class Meta:
		model = usuario
