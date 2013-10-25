#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class usuario(models.Model):
	usu_nombre		    = models.CharField(max_length=50)
	usu_apellido		= models.CharField(max_length=50)
	usu_correo		    = models.CharField(max_length=50)
	usu_nombreUsuario	= models.CharField(max_length=50)
	usu_fechanacimiento	= models.CharField(max_length=50)
	usu_clave		    = models.CharField(max_length=50)
	usu_direccion		= models.CharField(max_length=100)
	usu_twitter		    = models.CharField(max_length=50)
	usu_facebook		= models.CharField(max_length=50)
	usu_google		    = models.CharField(max_length=50)
	usu_privacidad		= models.CharField(max_length=50)
	usu_foto		    = models.ImageField(upload_to='imagenusuario')

	def __str__(self):
		return self.usu_nombre

class relacionUsuario(models.Model):
	cal_fecha		= models.ManyToManyField(usuario)

	def __str__(self):
		return self.cal_fecha


class calendario(models.Model):
	cal_fecha		= models.DateTimeField('date published')

	def __str__(self):
		return self.cal_fecha


class instagram(models.Model):
	ins_url			= models.CharField(max_length=200)

	def __str__(self):
		return self.ins_url


class soundcloud(models.Model):
	sou_url			= models.CharField(max_length=200)

	def __str__(self):
		return self.sou_url


class youtube(models.Model):
	you_url			= models.CharField(max_length=200)

	def __str__(self):
		return self.you_url


class album(models.Model):
	alb_nombre		    = models.CharField(max_length=100)
	alb_descripcion		= models.CharField(max_length=200)
	alb_privacidad		= models.BooleanField(default= True)
	alb_foto		    = models.ImageField(upload_to='imagenalbum')
	alb_fkusuario		= models.ForeignKey(usuario)
	alb_fkcalendario	= models.ForeignKey(calendario)

	def __str__(self):
		return self.alb_nombre


class comentario(models.Model):
	com_descripcion			= models.CharField(max_length=200)
	com_fkemisor	 		= models.ForeignKey(usuario)
	com_fkalbum				= models.ForeignKey(album)
	com_fkinstagram			= models.ForeignKey(instagram)
	com_fkyoutube			= models.ForeignKey(youtube)
	com_fksoundcloud		= models.ForeignKey(soundcloud)
	com_fkcalendario		= models.ForeignKey(calendario)
	
	def __str__(self):
		return self.com_descripcion


class meGusta(models.Model):
	mgu_like		= models.CharField(max_length=200)
	mgu_fkemisor	= models.ForeignKey(usuario)
	mgu_fkalbum				= models.ForeignKey(album)
	mgu_fkinstagram			= models.ForeignKey(instagram)
	mgu_fkyoutube			= models.ForeignKey(youtube)
	mgu_fksoundcloud		= models.ForeignKey(soundcloud)
	mgu_fkcalendario		= models.ForeignKey(calendario)

	def __str__(self):
		return self.mgu_like

class notificacion(models.Model):
	not_fkemisor			= models.ForeignKey(usuario)
	not_fkalbum				= models.ForeignKey(album)
	not_fkinstagram			= models.ForeignKey(instagram)
	not_fkyoutube			= models.ForeignKey(youtube)
	not_fksoundcloud		= models.ForeignKey(soundcloud)
	not_fkcalendario		= models.ForeignKey(calendario)
	def __str__(self):
		return self.not_id

class relacionNotificacion(models.Model):
	not_fknotificacion		= models.ManyToManyField(notificacion)

	def __str__(self):
		return self.mgu_like

class relacionComentario(models.Model):
	not_fkusuarioemisor		= models.ManyToManyField(comentario)

	def __str__(self):
		return self.mgu_like

