from appproyecto.models import usuario
from appproyecto.forms import registroForm
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from appproyecto.decorador import get_user_lazy
from django.shortcuts import render_to_response,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

def inicio(request):
	usuarios=usuario.objects.all()
	return render_to_response('plantilla.html',{'usuarios':usuarios},context_instance=RequestContext(request))

#Inicio Principal
def principalinicio(request):
	return render_to_response('principalinicio.html',context_instance=RequestContext(request))


@get_user_lazy
def autentificacionUsuario(request):
	from django.contrib.auth import get_user
	request.user = get_user(request)
	import pdb; pdb.set_trace()
	username = request.POST['usu_nombreUsuario']
	password = request.POST['usu_clave']
	user = authenticate(username=username, password=password)	
	if user is not None:
		login(request, user)
		
		return principalinicio(request)
	else:
		return HttpResponse(status=404)



def login_principal(request):
	return render_to_response('login_principal.html',context_instance=RequestContext(request))


def nuevo_usuario(request):
	if request.method=='POST':
		formulario = registroForm( request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/facebook')
	else:
		formulario = registroForm()
	return render_to_response('registrousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def usuario_consulta(request,id_usuario):
	usuario_det = usuario.objects.get(id= id_usuario)
	return render_to_response('usuario_consulta.html',{'usuario':usuario_det},context_instance=RequestContext(request))
