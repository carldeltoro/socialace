#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class usuario(models.Model):
	usu_nombre		= models.CharField(max_length=50)
	usu_apellido		= models.CharField(max_length=50)
	usu_correo		= models.CharField(max_length=50)
	usu_nombreUsuario	= models.CharField(max_length=50)
	usu_clave		= models.CharField(max_length=50)
	usu_direccion		= models.CharField(max_length=100)
	usu_twitter		= models.CharField(max_length=50)
	usu_facebook		= models.CharField(max_length=50)
	usu_google		= models.CharField(max_length=50)
	usu_privacidad		= models.CharField(max_length=50)
	usu_foto		= models.ImageField(upload_to='imagenusuario')
	usu_status		= models.BooleanField(default=True)
	usu_fkusuario		= models.ForeignKey(usuario)
	def __str__(self):
		return self.usu_nombre


class album(models.Model):
	alb_nombre		= models.CharField(max_length=100)
	alb_descripcion		= models.CharField(max_length=200)
	alb_privacidad		= models.CharField(max_length=200)
	alb_foto		= models.BooleanField(default=True)
	alb_fkusuario		= models.ForeignKey(usuario)
	alb_fkcalendario	= models.ForeignKey(calendario)
	def __str__(self):
		return self.alb_nombre


class notificacion(models.Model):
	not_fkusuarioemisor		= models.ForeignKey(usuario)
	not_fkusuarioreceptor	= models.ForeignKey(usuario)
	not_fkalbum				= models.ForeignKey(album)
	not_fknotificacion		= models.ForeignKey(notificacion)
	not_fkinstagram			= models.ForeignKey(instagram)
	not_fkyoutube			= models.ForeignKey(youtube)
	not_fksoundcloud		= models.ForeignKey(soundcloud)
	not_fkcalendario		= models.ForeignKey(calendario)
	def __str__(self):
		return self.not_id

class comentario(models.Model):
	com_descripcion			= models.CharField(max_length=200)
	com_fkusuarioemisor		= models.ForeignKey(usuario)
	com_fkusuarioreceptor	= models.ForeignKey(usuario)
	com_fkalbum				= models.ForeignKey(album)
	com_fkcomentario		= models.ForeignKey(comentario)
	com_fkinstagram			= models.ForeignKey(instagram)
	com_fkyoutube			= models.ForeignKey(youtube)
	com_fksoundcloud		= models.ForeignKey(soundcloud)
	com_fkcalendario		= models.ForeignKey(calendario)
	
	def __str__(self):
		return self.com_descripcion

class megusta(models.Model):
	mgu_like		= models.CharField(max_length=200)
	mgu_fkusuarioemisor		= models.ForeignKey(usuario)
	mgu_fkusuarioreceptor	= models.ForeignKey(usuario)
	mgu_fkalbum				= models.ForeignKey(album)
	mgu_fkinstagram			= models.ForeignKey(instagram)
	mgu_fkyoutube			= models.ForeignKey(youtube)
	mgu_fksoundcloud		= models.ForeignKey(soundcloud)
	mgu_fkcalendario		= models.ForeignKey(calendario)

	def __str__(self):
		return self-mgu_like
class calendario(models.Model):
	cal_fecha		= models.DateTimeField('date published')
	def __str__(self):
		return self.cal_fecha

class instagram(models.Model):
	ins_url			= models.CharField(max_length=200)
	album			= models.ManyToManyField(album)
	def __str__(self):
		return self.ins_url

class soundcloud(models.Model):
	sou_url			= models.CharField(max_length=200)
	album			= models.ManyToManyField(album)
	def __str__(self):
		return self.sou_url

class youtube(models.Model):
	you_url			= models.CharField(max_length=200)
	album			= models.ManyToManyField(album)
	def __str__(self):
		return self.you_url



