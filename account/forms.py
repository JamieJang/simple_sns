from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from blog.models import Profile

class SignupForm( UserCreationForm ):
	username = forms.CharField(max_length=20,
							 widget=forms.TextInput(
							 	attrs={
							 		'class':'form-control',
							 		'placeholder':'ID',							 		
							 	}))
	password1 = forms.CharField(widget=forms.PasswordInput(
							attrs={
							'class':'form-control',
							'placeholder':'Password',
							}))
	password2 = forms.CharField(widget=forms.PasswordInput(
							attrs={
							'class':'form-control',
							'placeholder':'Password Confirm',
							}))

	prof_img = forms.ImageField(required=False, widget=forms.FileInput(
							attrs={
							'class':'form-control',
							'id':'prof_img',
							'placeholder':'Choice profile photo',
							}))
	name = forms.CharField(required=False, max_length=256,
						widget=forms.TextInput(
						attrs={
							'class':'form-control',
							'placeholder':'Name',
						}))

	class Meta:
		model = User
		fields = ('prof_img','username','password1','password2','name')

class ProfileForm(forms.ModelForm):
	prof_img = forms.ImageField(required=False, widget=forms.FileInput(
							attrs={
							'class':'form-control',
							'id':'prof_img',
							'placeholder':'Choice profile photo',
							}))
	name = forms.CharField(required=False, max_length=256,
						widget=forms.TextInput(
						attrs={
							'class':'form-control',
							'placeholder':'Name',
						}))
	class Meta:
		model = Profile
		fields = ('prof_img', 'name')