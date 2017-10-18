from django import forms

from .models import Post, Tag, Profile, Group

class PostForm(forms.ModelForm):

	content = forms.CharField(widget=forms.Textarea(
								attrs = {
									'id':'content',
								}))
	location = forms.CharField(max_length=1024,
							widget=forms.TextInput(
								attrs={
									'id':'location',
								}))
	tags = forms.CharField(required=False,widget=forms.TextInput(
						attrs={
							'id':'tags',
							'placeholder':'Write tags seperate with comma'
						}))
	
	class Meta:
		model = Post
		fields = ['content','location','tags']