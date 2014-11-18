from django import forms
from .models import Categorias, Audio, Videos, Imagenes, Comentario

class categoriasForm (forms.ModelForm):

	titulo    =   forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}))

	class Meta:
		model = Categorias


class audiosForm(forms.ModelForm):
		
	titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}))
	descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}))
	urll = forms.FileField(required=False)

	class Meta:
		model = Audio
		exclude = ('usuario',)


class videosForm(forms.ModelForm):
		
	titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}))
	descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}))
	urll = forms.FileField(required=False)

	class Meta:
		model = Videos
		exclude = ('usuario',)


class imagenesForm(forms.ModelForm):
		
	titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}))
	descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}))
	urllalta = forms.FileField(required=False)
	urllbaja = forms.FileField(required=False)

	class Meta:
		model = Imagenes
		exclude = ('usuario',)

class comentarioForm(forms.ModelForm):
	mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

	class Meta:
		model = Comentario
		exclude = ('usuario','id_multimedia',)






