from django.contrib import admin

from .models import  Categorias, Videos, Audio, Imagenes, Comentario


admin.site.register(Categorias)
admin.site.register(Videos)
admin.site.register(Audio)
admin.site.register(Imagenes)
admin.site.register(Comentario)
