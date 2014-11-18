from django.contrib import admin

from .models import  permisos, permisos_usuarios

'''class permisosUsers(admin.ModelAdmin):
		list_display = ('permiso', 'usuario',)'''


admin.site.register(permisos)
admin.site.register(permisos_usuarios)


