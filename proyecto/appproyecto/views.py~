from appproyecto.models import usuario
from appproyecto.forms import registroForm
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def inicio(request):
	usuarios=usuario.objects.all()
	return render_to_response('login.html',{'usuarios':usuarios},context_instance=RequestContext(request))


def loginfacebook(request):
	return render_to_response('loginfacebook.html',context_instance=RequestContext(request))

def nuevo_usuario(request):
	if request.method=='POST':
		formulario = registroForm( request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/facebook')
	else:
		formulario = registroForm()
	return render_to_response('registroplantilla.html',{'formulario':formulario}, context_instance=RequestContext(request))


