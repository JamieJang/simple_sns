from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

class Group(models.Model):
	name = models.CharField(max_length=256, unique=True)

	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	prof_img = models.ImageField(null=True, blank=True, upload_to='blog')
	name = models.CharField(max_length=128,blank=True)
	group = models.ManyToManyField(Group, blank=True)

	def __str__(self):
		return self.name

	@receiver(post_save,sender=User)
	def update_user_profile(sender,instance,created,**kwargs):
		if created:
			Profile.objects.create(user=instance)
		instance.profile.save()


class Tag(models.Model):
	name = models.CharField(max_length=256,unique=True)

	def __str__(self):
		return self.name


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	location = models.CharField(max_length=256)	
	q_location = models.SlugField(allow_unicode=True)
	content = models.TextField()
	tags = models.ManyToManyField(Tag,blank=True)
	published = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content[:15]

	def save(self):
		self.q_location = self.location.replace(' ','-')
		super(Post,self).save()
	class Meta:
		ordering = ['-published']
