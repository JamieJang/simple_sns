from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, View


from decouple import config

from .models import Post, Tag, Profile, Group
from .forms import PostForm


class Index(ListView):
	def get(self,request):
		if request.user.is_anonymous:
			return redirect('account:signup')
		else:
			form = PostForm()
			posts = Post.objects.prefetch_related('tags').select_related('author').all()
			profile = Profile.objects.select_related('user').filter(user=request.user)
			return render(request,'blog/index.html', {'posts':posts,
													'form':form,
													'profile':profile[0],
													'apikey':config('API_KEY')})
	def post(self,request):
		form = PostForm(request.POST)
		if form.is_valid():
			user = request.user
			content = request.POST.get('content')
			location = request.POST.get('location').replace(',',' ')
			tmp = request.POST.get('tags').split(',')
			post = Post(author=user,content=content,location=location)
			post.save()
			for each in tmp:				
				each = each.strip().replace(' ','_')
				t = Tag.objects.get_or_create(name=each)
				t[0].save()
				post.tags.add(t[0])

		return redirect('blog:index')


class MyProfile(ListView):

	def get(self,request, user):
		if request.user.is_anonymous:
			return redirect('account:login')
		elif request.user.username == user:
			form = PostForm()
			profile = Profile.objects.select_related('user').filter(user__username=user)
			posts = Post.objects.prefetch_related('tags').select_related('author').filter(author__username=user)
			return render(request,'blog/profile.html', {'profile':profile[0],
													'posts':posts,
													'form':form})

		profile = Profile.objects.select_related('user').filter(user__username=user)
		posts = Post.objects.prefetch_related('tags').select_related('author').filter(author__username=user)
		return render(request,'blog/profile.html', {'profile':profile[0],
												'posts':posts,
												'form':False})

	def post(self,request,user):
		form = PostForm(request.POST)
		if form.is_valid():
			user = request.user
			content = request.POST.get('content')
			location = request.POST.get('location').replace(',',' ')
			tmp = request.POST.get('tags').split(',')
			post = Post(author=user,content=content,location=location)
			post.save()
			for each in tmp:				
				each = each.strip().replace(' ','_')
				t = Tag.objects.get_or_create(name=each)
				t[0].save()
				post.tags.add(t[0])

		return redirect('blog:profile',user)

class SearchingTag(ListView):
	def get(self,request,tag):
		form = PostForm()
		posts = Post.objects.prefetch_related('tags').select_related('author').filter(tags__name__icontains=tag)
		profile = Profile.objects.select_related('user').filter(user=request.user)
		return render(request,'blog/index.html', {'posts':posts,
												'form':form,
												'profile':profile[0],
												'apikey':config('API_KEY')})
		
	def post(self,request,tag):
		form = PostForm(request.POST)
		if form.is_valid():
			user = request.user
			content = request.POST.get('content')
			location = request.POST.get('location').replace(',',' ')
			tmp = request.POST.get('tags').split(',')
			post = Post(author=user,content=content,location=location)
			post.save()
			for each in tmp:				
				each = each.strip().replace(' ','_')
				t = Tag.objects.get_or_create(name=each)
				t[0].save()
				post.tags.add(t[0])

		return redirect('blog:index')

class SearchingLocation(ListView):
	def get(self,request,qlocation):
		form = PostForm()
		posts = Post.objects.prefetch_related('tags').select_related('author').filter(q_location__icontains=qlocation)
		profile = Profile.objects.select_related('user').filter(user=request.user)
		return render(request,'blog/index.html', {'posts':posts,
												'form':form,
												'profile':profile[0],
												'apikey':config('API_KEY')})

	def post(self,request,qlocation):
		form = PostForm(request.POST)
		if form.is_valid():
			user = request.user
			content = request.POST.get('content')
			location = request.POST.get('location').replace(',',' ')
			tmp = request.POST.get('tags').split(',')
			post = Post(author=user,content=content,location=location)
			post.save()
			for each in tmp:				
				each = each.strip().replace(' ','_')
				t = Tag.objects.get_or_create(name=each)
				t[0].save()
				post.tags.add(t[0])

		return redirect('blog:index')

class RemovePost(ListView):
	def get(self,request,pk):
		post = Post.objects.filter(pk=pk)
		post.delete()
		referer = request.META.get('HTTP_REFERER')
		return redirect(referer)

class ModifyPost(ListView):
	def get(self,request,pk):		
		post = Post.objects.select_related('author').filter(pk=pk)[0]
		if request.user.id == post.author.id:
			form = PostForm()
			profile = Profile.objects.select_related('user').filter(user=request.user)
			return render(request,'blog/modify.html', {'post':post, 'form':form,
													'profile':profile[0],
													'apikey':config('API_KEY')})
		else:
			return HttpResponse("Error")

	def post(self,request, pk):
		post = Post.objects.select_related('author').filter(pk=pk)[0]
		if post.author.id == request.user.id:
			form = PostForm(request.POST)
			if form.is_valid():				
				content = request.POST.get('content')
				location = request.POST.get('location').replace(',','')
				tmp = request.POST.get('tags').split(',')
				if tmp[-1] == '':
					tmp = tmp[:-1]
				if content != post.content:
					post.content = content
				if location != post.location:
					post.location = location	
				post.save()
				print("tmp:",tmp)

				for t in post.tags.all():
					if t.name in tmp:
						tmp.remove(t.name)
				if tmp:		
					for each in tmp:
						each = each.strip().replace(' ','_')
						t = Tag.objects.get_or_create(name=each)[0]
						t.save()
						post.tags.add(t)
		return redirect('blog:index')

class Searching(ListView):
	def get(self,request):
		q = request.GET.get('query')
		loc_q = Post.objects.prefetch_related('tags').select_related('author').filter(location__icontains=q)
		tag_q = Post.objects.prefetch_related('tags').select_related('author').filter(tags__name__icontains=q)
		posts = (loc_q | tag_q).distinct().order_by('-published')

		form = PostForm()
		profile = Profile.objects.select_related('user').filter(user=request.user)
		return render(request,'blog/index.html', {'posts':posts,
												'form':form,
												'profile':profile[0],
												'apikey':config('API_KEY')})


		
		
		