from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import permisos_usuarios


# funcion para retornar todas las variables que utilizare repetidas veces en todo el sitio web
# Function to return all who uses variables repeatedly throughout the web site
@login_required
def my_processor(request):

	emedio = "no"
	eusuario = "no"
	epermisousuarios = "no"
	editarmedios = "no"
	crearmedios = "no"
	crearcategoria = "no"
	editarcategoria = "no"
	crearusuario = "no"
	editarusuario = "no"
	descargarmedios = "no"

	permisos = permisos_usuarios.objects.filter(Q(permiso__titulo__contains='medios') & Q(usuario=request.user.id))

	if len(permisos) != 0:
		emedio = "yes"

	permisos = permisos_usuarios.objects.filter(Q(permiso__titulo__contains='usuarios') & Q(usuario=request.user.id))

	if len(permisos) != 0:
		eusuario = "yes"

	permisos = permisos_usuarios.objects.filter(Q(permiso__titulo__contains='permisos') & Q(usuario=request.user.id))

	if len(permisos) != 0:
		epermisousuarios = "yes"

	#-----------------------------------------------------------------------------------

	permisos = permisos_usuarios.objects.filter(Q(permiso__titulo__contains='Crear categorias') & Q(usuario=request.user.id))

	if len(permisos) != 0:
		crearcategoria = "yes"

	permisos = permisos_usuarios.objects.filter(Q(permiso__titulo__contains='Editar categorias') & Q(usuario=request.user.id))

	if len(permisos) != 0:
		editarcategoria = "yes"
		

	permisos = permisos_usuarios.objects.filter(Q(permiso__titulo__contains='Crear medios') & Q(usuario=request.user.id))

	if len(permisos) != 0:
		crearmedios = "yes"

	permisos = permisos_usuarios.objects.filter(Q(permiso__titulo__contains='Modificar medios') & Q(usuario=request.user.id))

	if len(permisos) != 0:
		editarmedios = "yes"

	permisos = permisos_usuarios.objects.filter(Q(permiso__titulo__contains='Crear usuarios') & Q(usuario=request.user.id))

	if len(permisos) != 0:
		crearusuario = "yes"

	permisos = permisos_usuarios.objects.filter(Q(permiso__titulo__contains='Modificar usuarios') & Q(usuario=request.user.id))

	if len(permisos) != 0:
		editarusuario = "yes"

	permisos = permisos_usuarios.objects.filter(Q(permiso__titulo__contains='Descargar medios') & Q(usuario=request.user.id))

	if len(permisos) != 0:
		descargarmedios = "yes"




	menu = ({
        'emedio': emedio,
        'eusuario': eusuario,
        'epermisousuarios': epermisousuarios,
        'editarmedios':editarmedios,
        'crearmedios': crearmedios,
        'crearcategoria':crearcategoria,
        'editarcategoria':editarcategoria,
        'crearusuario':crearusuario,
        'editarusuario': editarusuario,
        'descargarmedios': descargarmedios    
        })	
	return {'menu': menu }





