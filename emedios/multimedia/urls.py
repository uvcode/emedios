from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^panel/editcategorias/$', 'multimedia.views.editcategorias_view', name='Editar categorias'), 

	url(r'^panel/editvideos/$', 'multimedia.views.editvideos_view', name='Editar videos'), 

	url(r'^panel/editvideos/buscar/$', 'multimedia.views.editvideosbuscar_view', name='Buscar editvideos'),

	url(r'^panel/editimagenes/$', 'multimedia.views.editimagenes_view', name='Editar imagenes'),

	url(r'^panel/editimagenes/buscar/$', 'multimedia.views.editimagenesbuscar_view', name='Buscar editimagenes'), 

	url(r'^panel/editaudios/$', 'multimedia.views.editaudios_view', name='Editar audio'), 

	url(r'^panel/editaudios/buscar/$', 'multimedia.views.editaudiosbuscar_view', name='Buscar editaudios'),

	url(r'^panel/dvideos/$', 'multimedia.views.dvideos_view', name='videos'), 

	url(r'^panel/dvideos/buscar/$', 'multimedia.views.dvideosbuscar_view', name='Buscar videos'),

	url(r'^panel/dvideos/vervideo/(?P<id_video>\d+)/$', 'multimedia.views.vervideo_view', name='Ver video'), 

	url(r'^panel/dimagenes/$', 'multimedia.views.dimagenes_view', name='imagenes'), 

	url(r'^panel/dimagenes/buscar/$', 'multimedia.views.dimagenesbuscar_view', name='Buscar imagenes'),

	url(r'^panel/daudio/$', 'multimedia.views.daudio_view', name='audio'), 

	url(r'^panel/daudio/buscar/$', 'multimedia.views.daudiobuscar_view', name='Buscar audio'),

	url(r'^panel/editcategorias/editcategoria/(?P<id_categoria>\d+)/$', 'multimedia.views.editcategoria_view', name='Editar categoria'), 

	url(r'^panel/editcategorias/nuevacategoria/$', 'multimedia.views.nuevacategoria_view', name='Nueva categoria'), 

	url(r'^panel/editaudios/editaudio/(?P<id_audio>\d+)/$', 'multimedia.views.editaudio_view', name='Editar audio'), 

	url(r'^panel/editaudios/nuevoaudio/$', 'multimedia.views.nuevoaudio_view', name='Nuevo audio'), 

	url(r'^panel/editvideos/editvideo/(?P<id_video>\d+)/$', 'multimedia.views.editvideo_view', name='Editar video'), 

	url(r'^panel/editvideos/nuevovideo/$', 'multimedia.views.nuevovideo_view', name='Nuevo video'), 

	url(r'^panel/editimagenes/editimagen/(?P<id_imagen>\d+)/$', 'multimedia.views.editimagen_view', name='Editar imagen'), 

	url(r'^panel/editimagenes/nuevaimagen/$', 'multimedia.views.nuevaimagen_view', name='Nueva imagen'), 

)

