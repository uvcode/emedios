from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .context_processors import my_processor
from django.http import HttpResponseRedirect
from .forms import usuariosForm, newusuarioForm, permisosForm
from django.contrib import messages
from .models import permisos_usuarios, permisos
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm


@login_required
def usuarios_view(request):
	
	diccionarios = my_processor(request)
	menu = diccionarios['menu']

	if menu['eusuario'] != 'no' or  menu['epermisousuarios'] != 'no':
		usuarios = User.objects.all()
		return render(request,'login/usuarios.html',{ 'usuarios': usuarios })
	else:
		return HttpResponseRedirect('/panel/')

@login_required
def editpermisos_view(request, id_usuario):

	permiso = permisos_usuarios.objects.get(usuario=id_usuario)

	if permiso != None:
		if request.method == "POST":
			form = permisosForm(request.POST,instance=permiso)
			if form.is_valid():
				edit_perm = form.save(commit=False)
				form.save_m2m()
				edit_perm.save

			return HttpResponseRedirect('/panel/usuarios/')
		else:
			form = permisosForm(instance=permiso)

	ctx = {'form': form, }
	return render(request,'login/editpermisos.html', ctx  )



@login_required
def editusuario_view(request, id_usuario):

    usuario =  User.objects.get(id=id_usuario)

    if request.method == 'POST':
    	usuario_Form = usuariosForm(request.POST)


    	if usuario_Form.is_valid():
	    	usuario.email = usuario_Form.cleaned_data['email']
	    	usuario.first_name = usuario_Form.cleaned_data['first_name']
	    	usuario.last_name = usuario_Form.cleaned_data['last_name']
	    		#usuario.password = usuariosForm.cleaned_data['password_one']
	    	usuario.save()
    		return HttpResponseRedirect('/panel/usuarios/')
    	else:
    		messages.error(request, "Error")


    elif request.method == 'GET':

        usuario_Form = usuariosForm(initial={
            'email': usuario.email,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            })


    return render(request,'login/editusuario.html', { 'usuario_Form': usuario_Form, 'usuario': usuario })

@login_required
def login_view(request):
	return render(request, 'multimedia/dimagenes.html')

@login_required
def nuevousuario_view(request):
	if request.method == 'POST':
		form = newusuarioForm(request.POST or None)
		if form.is_valid():
			form.save()
			us = User.objects.get(username=form.cleaned_data['username'])
			u = permisos_usuarios(usuario_id = int(us.id))
			u.save()
			return HttpResponseRedirect('/panel/usuarios/')
	else:
		form = newusuarioForm()

	return render(request, 'login/usuario.html',{'form':form})











