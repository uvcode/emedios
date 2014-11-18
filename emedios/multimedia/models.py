from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
	titulo = models.CharField(max_length=300, unique=True)

	def __unicode__(self):
		return self.titulo


class Videos(models.Model):
	titulo = models.CharField(max_length=300, unique=True)
	categoria = models.ForeignKey(Categorias)
	descripcion =  models.TextField(blank=True, null=True)
	urll = models.FileField(upload_to='videos/', null=True, blank=True)
	fechadecreacion = models.DateField(auto_now_add= True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo

class Audio(models.Model):
	titulo = models.CharField(max_length=300, unique=True)
	categoria = models.ForeignKey(Categorias)
	descripcion =  models.TextField(blank=True, null=True)
	urll = models.FileField(upload_to='audios/', null=True, blank=True)
	fechadecreacion = models.DateField(auto_now_add= True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo


class Imagenes(models.Model):
	titulo = models.CharField(max_length=300, unique=True)
	categoria = models.ForeignKey(Categorias)
	descripcion =  models.TextField(blank=True, null=True)
	urllalta = models.FileField(upload_to='image/', null=True, blank=True)
	urllbaja = models.FileField(upload_to='image/', null=True, blank=True)
	fechadecreacion = models.DateField(auto_now_add= True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return self.titulo

class Comentario(models.Model):
    fechadecreacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User)
    mensaje = models.TextField()
    id_multimedia = models.ForeignKey(Videos)

    def __unicode__(self):
        return self.mensaje[:25]
