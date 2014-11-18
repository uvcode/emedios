from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Videos, Categorias, Audio, Imagenes, Comentario
from .forms import categoriasForm, audiosForm, videosForm, imagenesForm, comentarioForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime


@login_required
def login_view(request):
	return render(request, 'login/usuario.html')

@login_required
def dvideos_view(request):
	videos =  Videos.objects.all().order_by('fechadecreacion', 'id').reverse()
	return render(request, 'multimedia/dvideos.html',{'videos': videos})

@login_required
def dvideosbuscar_view(request):
	titulo = request.POST['titulo']
	fecha = request.POST['fecha']
	videos = {}
	if fecha:
		dt = datetime.strptime(str(fecha), "%d-%m-%Y")

	if titulo:

		if fecha:
			videos = Videos.objects.filter(Q(titulo__contains=titulo) & Q(fechadecreacion=dt))
		else:
			videos = Videos.objects.filter(titulo__contains=titulo)

	elif fecha:
		videos = Videos.objects.filter(fechadecreacion=dt)

	return render(request, 'multimedia/dvideos.html',{'videos': videos})

@login_required
def vervideo_view(request, id_video):
	user = User.objects.get(pk=request.user.id)
	video =  Videos.objects.get(id=id_video)
	comentario = Comentario.objects.filter(id_multimedia=id_video).order_by('fechadecreacion', 'id').reverse()

	if request.method == 'POST':
		comentario_Form = comentarioForm(request.POST)
		if comentario_Form.is_valid():
			cform = comentario_Form.save(commit=False)
			cform.usuario = user
			cform.id_multimedia = video
			cform.save()
			return HttpResponseRedirect('/panel/dvideos/vervideo/'+id_video+'/')
	else:
		comentario_Form = comentarioForm()

	return render(request, 'multimedia/vervideo.html',{'video': video, 'comentario': comentario, 'comentario_Form':comentario_Form})


@login_required
def dimagenes_view(request):
	imagenes =  Imagenes.objects.all().order_by('fechadecreacion', 'id').reverse()
	return render(request, 'multimedia/dimagenes.html',{'imagenes':imagenes})

@login_required
def dimagenesbuscar_view(request):
	titulo = request.POST['titulo']
	fecha = request.POST['fecha']
	imagenes = {}
	if fecha:
		dt = datetime.strptime(str(fecha), "%d-%m-%Y")

	if titulo:

		if fecha:
			imagenes = Imagenes.objects.filter(Q(titulo__contains=titulo) & Q(fechadecreacion=dt))
		else:
			imagenes = Imagenes.objects.filter(titulo__contains=titulo)

	elif fecha:
		imagenes = Imagenes.objects.filter(fechadecreacion=dt)

	return render(request, 'multimedia/dimagenes.html',{'imagenes':imagenes})

@login_required
def daudio_view(request):
	audio = Audio.objects.all().order_by('fechadecreacion', 'id').reverse()
	return render(request, 'multimedia/daudio.html',{'audio': audio})

@login_required
def daudiobuscar_view(request):
	titulo = request.POST['titulo']
	fecha = request.POST['fecha']
	audio = {}
	if fecha:
		dt = datetime.strptime(str(fecha), "%d-%m-%Y")

	if titulo:

		if fecha:
			audio = Audio.objects.filter(Q(titulo__contains=titulo) & Q(fechadecreacion=dt))
		else:
			audio = Audio.objects.filter(titulo__contains=titulo)

	elif fecha:
		audio = Audio.objects.filter(fechadecreacion=dt)

	return render(request, 'multimedia/daudio.html',{'audio': audio})

@login_required
def editcategorias_view(request):
	categorias = Categorias.objects.all()
	return render(request, 'multimedia/editcategorias.html',{'categorias': categorias})

@login_required
def editvideos_view(request):
	videos = Videos.objects.all().order_by('fechadecreacion', 'id').reverse()
	return render(request, 'multimedia/editvideos.html', {'videos': videos })

@login_required
def editvideosbuscar_view(request):
	titulo = request.POST['titulo']
	fecha = request.POST['fecha']
	videos = {}
	if fecha:
		dt = datetime.strptime(str(fecha), "%d-%m-%Y")

	if titulo:

		if fecha:
			videos = Videos.objects.filter(Q(titulo__contains=titulo) & Q(fechadecreacion=dt))
		else:
			videos = Videos.objects.filter(titulo__contains=titulo)

	elif fecha:
		videos = Videos.objects.filter(fechadecreacion=dt)

	return render(request, 'multimedia/editvideos.html', {'videos': videos })

@login_required
def editimagenes_view(request):
	imagenes = Imagenes.objects.all().order_by('fechadecreacion','id').reverse()
	return render(request, 'multimedia/editimagenes.html',{'imagenes':imagenes})

@login_required
def editimagenesbuscar_view(request):
	titulo = request.POST['titulo']
	fecha = request.POST['fecha']
	imagenes = {}
	if fecha:
		dt = datetime.strptime(str(fecha), "%d-%m-%Y")

	if titulo:

		if fecha:
			imagenes = Imagenes.objects.filter(Q(titulo__contains=titulo) & Q(fechadecreacion=dt))
		else:
			imagenes = Imagenes.objects.filter(titulo__contains=titulo)

	elif fecha:
		imagenes = Imagenes.objects.filter(fechadecreacion=dt)

	return render(request, 'multimedia/editimagenes.html',{'imagenes':imagenes})

@login_required
def editaudios_view(request):
	audio = Audio.objects.all().order_by('fechadecreacion', 'id').reverse()
	return render(request, 'multimedia/editaudios.html',{'audio': audio})

@login_required
def editaudiosbuscar_view(request):
	titulo = request.POST['titulo']
	fecha = request.POST['fecha']
	audio = {}
	if fecha:
		dt = datetime.strptime(str(fecha), "%d-%m-%Y")

	if titulo:

		if fecha:
			audio = Audio.objects.filter(Q(titulo__contains=titulo) & Q(fechadecreacion=dt))
		else:
			audio = Audio.objects.filter(titulo__contains=titulo)

	elif fecha:
		audio = Audio.objects.filter(fechadecreacion=dt)

	return render(request, 'multimedia/editaudios.html',{'audio': audio})

@login_required
def editcategoria_view(request, id_categoria):

    categoria =  Categorias.objects.get(id=id_categoria)

    if request.method == 'POST':
    	categoria_Form = categoriasForm(request.POST)


    	if categoria_Form.is_valid():
	    	categoria.titulo = categoria_Form.cleaned_data['titulo']
	    	categoria.save()
    		return HttpResponseRedirect('/panel/editcategorias/')
    	else:
    		messages.error(request, "Error")


    elif request.method == 'GET':

        categoria_Form = categoriasForm(initial={
            'titulo': categoria.titulo,
            })


    return render(request,'multimedia/editcategoria.html', { 'categoria_Form': categoria_Form })

@login_required
def nuevacategoria_view(request):
	if request.method == 'POST':
		categoria_Form = categoriasForm(request.POST)
		if categoria_Form.is_valid():
			categoria_Form.save()
			return HttpResponseRedirect('/panel/editcategorias/')
	else:
		categoria_Form = categoriasForm()

	return render(request, 'multimedia/editcategoria.html',{'categoria_Form':categoria_Form})



@login_required
def editaudio_view(request, id_audio):

    audio =  Audio.objects.get(id=id_audio)

    if request.method == 'POST':
    	audio_Form = audiosForm(request.POST, request.FILES, instance=audio)


    	if audio_Form.is_valid():
    		audio.titulo = audio_Form.cleaned_data['titulo']
    		audio.categoria = audio_Form.cleaned_data['categoria']
    		audio.descripcion = audio_Form.cleaned_data['descripcion']
    		archivo = audio_Form.cleaned_data['urll']

    		if archivo:
    			audio.urll = archivo
	    	audio.save()
    		return HttpResponseRedirect('/panel/editaudios/')
    	else:
    		messages.error(request, "Error")


    elif request.method == 'GET':

    	audio_Form = audiosForm(instance=audio)

		


    return render(request,'multimedia/editaudio.html', { 'audio_Form': audio_Form })


@login_required
def nuevoaudio_view(request):
	user = User.objects.get(pk=request.user.id)

	if request.method == 'POST':
		audio_Form = audiosForm(request.POST, request.FILES)
		if audio_Form.is_valid():
			aform = audio_Form.save(commit=False)
			aform.usuario = user
			aform.save()
			return HttpResponseRedirect('/panel/editaudios/')
	else:
		audio_Form = audiosForm()

	return render(request, 'multimedia/editaudio.html',{'audio_Form':audio_Form})


@login_required
def editvideo_view(request, id_video):

    video =  Videos.objects.get(id=id_video)

    if request.method == 'POST':
    	video_Form = videosForm(request.POST, request.FILES, instance=video)


    	if video_Form.is_valid():
    		video.titulo = video_Form.cleaned_data['titulo']
    		video.categoria = video_Form.cleaned_data['categoria']
    		video.descripcion = video_Form.cleaned_data['descripcion']
    		archivo = video_Form.cleaned_data['urll'] 

    		if archivo:
    			video.urll = archivo
	    	video.save()
    		return HttpResponseRedirect('/panel/editvideos/')
    	else:
    		messages.error(request, "Error")


    elif request.method == 'GET':

    	video_Form = videosForm(instance=video)

		


    return render(request,'multimedia/editvideo.html', { 'video_Form': video_Form })



@login_required
def nuevovideo_view(request):
	user = User.objects.get(pk=request.user.id)

	if request.method == 'POST':
		video_Form = videosForm(request.POST, request.FILES)
		if video_Form.is_valid():
			vform = video_Form.save(commit=False)
			vform.usuario = user
			vform.save()
			return HttpResponseRedirect('/panel/editvideos/')
	else:
		video_Form = videosForm()

	return render(request, 'multimedia/editvideo.html',{'video_Form':video_Form})


@login_required
def editimagen_view(request, id_imagen):

    imagen =  Imagenes.objects.get(id=id_imagen)

    if request.method == 'POST':
    	imagen_Form = imagenesForm(request.POST, request.FILES, instance=imagen)


    	if imagen_Form.is_valid():
    		imagen.titulo = imagen_Form.cleaned_data['titulo']
    		imagen.categoria = imagen_Form.cleaned_data['categoria']
    		imagen.descripcion = imagen_Form.cleaned_data['descripcion']
    		archivo = imagen_Form.cleaned_data['urllalta'] 
    		archivo2 = imagen_Form.cleaned_data['urllbaja'] 

    		if archivo:
    			imagen.urll = archivo
    		if archivo2:
    			imagen.urll = archivo
	    	imagen.save()
    		return HttpResponseRedirect('/panel/editimagenes/')
    	else:
    		messages.error(request, "Error")


    elif request.method == 'GET':

    	imagen_Form = imagenesForm(instance=imagen)

		


    return render(request,'multimedia/editimagen.html', { 'imagen_Form': imagen_Form })




@login_required
def nuevaimagen_view(request):
	user = User.objects.get(pk=request.user.id)

	if request.method == 'POST':
		imagen_Form = imagenesForm(request.POST, request.FILES)
		if imagen_Form.is_valid():
			imgform = imagen_Form.save(commit=False)
			imgform.usuario = user
			imgform.save()
			return HttpResponseRedirect('/panel/editimagenes/')
	else:
		imagen_Form = imagenesForm()

	return render(request, 'multimedia/editimagen.html',{'imagen_Form':imagen_Form})



