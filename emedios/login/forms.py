# -*- encoding: utf-8 -*-

from django import forms
from .models import permisos_usuarios, permisos
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class usuariosForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name','email') # le defino los campos del modelo que voy a modificar.
	
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))


class newusuarioForm(UserCreationForm):
		
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario','name': 'Nombre de usuario'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar contraseña'}))

	class Meta:
		model = User
		fields = ('username','first_name', 'last_name','email','password1','password2')

	def save(self, commit=True):
		user = super(newusuarioForm, self).save(commit=False)
		user.email = self.cleaned_data["email"]
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]

		if commit:
			user.save()
		return user
	


class permisosForm (forms.ModelForm):

	permiso    =   forms.ModelMultipleChoiceField(queryset=permisos.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)

	class Meta:
		model = permisos_usuarios
		exclude = ('usuario',)


