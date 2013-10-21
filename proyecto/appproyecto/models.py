#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class usuario(models.Model):
	usu_id			= models.CharField(max_length=100)
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
	def __str__(self):
		return self.usu_nombre


class album(models.Model):
	alb_id			= models.CharField(max_length=100)
	alb_nombre		= models.CharField(max_length=100)
	alb_descripcion		= models.CharField(max_length=200)
	alb_privacidad		= models.CharField(max_length=200)
	alb_foto		= models.BooleanField(default=True)
	def __str__(self):
		return self.alb_nombre


class notificacion(models.Model):
	not_id		= models.CharField(max_length=100)
	def __str__(self):
		return self.not_id

class comentario(models.Model):
	com_id			= models.CharField(max_length=100)
	com_descripcion		= models.CharField(max_length=200)
	def __str__(self):
		return self.com_descripcion

class megusta(models.Model):
	mgu_id			= models.CharField(max_length=100)
	mgu_like		= models.CharField(max_length=200)
	def __str__(self):
		return self-mgu_like
class calendario(models.Model):
	cal_id			= models.CharField(max_length=100)
	cal_fecha		= models.DateTimeField('date published')
	def __str__(self):
		return self.cal_fecha

class instagram(models.Model):
	ins_id			= models.CharField(max_length=100)
	ins_url			= models.CharField(max_length=200)
	def __str__(self):
		return self.ins_url

class soundcloud(models.Model):
	sou_id			= models.CharField(max_length=100)
	sou_url			= models.CharField(max_length=200)
	def __str__(self):
		return self.sou_url

class youtube(models.Model):
	you_id			= models.CharField(max_length=100)
	you_url			= models.CharField(max_length=200)
	def __str__(self):
		return self.you_url

class album_instagram(models.Model):
	albins_id		= models.CharField(max_length=100)
	def __str__(self):
		return self.albins_id

class album_soundcloud(models.Model):
	albsou_id		= models.CharField(max_length=100)
	def __str__(self):
		return self.albsou_id

class album_youtube(models.Model):
	albyou_id		= models.CharField(max_length=100)
	def __str__(self):
		return self.albyou_id
