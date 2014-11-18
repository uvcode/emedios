from django.db import models
from django.contrib.auth.models import User


class permisos(models.Model):
	titulo = models.CharField(max_length=300, unique=True)

	def __unicode__(self):
		return self.titulo


class permisos_usuarios(models.Model):
	usuario = models.ForeignKey(User)
	permiso = models.ManyToManyField(permisos, blank=True)
	

	def __unicode__(self):
		return '%s' % (self.usuario)


