from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',

   	url(r'^$', login, {'template_name': 'login/login.html', }, name="login"),

	url(r'^/$', login, {'template_name': 'login/login.html', }, name="login"),

	url(r'^panel/$', 'multimedia.views.dimagenes_view', name='validacion'),  

	url(r'^panel/usuarios/$', 'login.views.usuarios_view', name='editusuarios'), 

	url(r'^panel/usuarios/editusuario/(?P<id_usuario>\d+)/$', 'login.views.editusuario_view', name='editusuario'), 

	url(r'^panel/usuarios/editpermisos/(?P<id_usuario>\d+)/$', 'login.views.editpermisos_view', name='editpermisos'), 

	url(r'^panel/usuarios/nuevoUsuario/', 'login.views.nuevousuario_view', name='Nuevo Usuario'), 

	url(r'cerrar/$', logout, {'next_page': '/', }, name="logout"),  
)

