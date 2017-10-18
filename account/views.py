from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http import Http404, HttpResponse
from django.contrib import messages


from .forms import SignupForm, ProfileForm
from blog.models import Profile

class my_signup(ListView):
	def get(self, request):
		form  = SignupForm()
		return render(request,'account/signup.html',{'form':form})

	def post(self, request):
		form = SignupForm(request.POST,request.FILES)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user.profile.name = form.cleaned_data.get('name')
			user.profile.prof_img = form.cleaned_data.get('prof_img')
			user.save()
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect('blog:index')
		else:
			print(form.errors)
			return HttpResponse(form.errors, status=404)

class my_login(ListView):
	def get(self,request):
		if not request.user.is_anonymous:
			return redirect('blog:index')

		form = AuthenticationForm()
		return render(request,'account/login.html', {'form':form})

	def post(self,request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('blog:index')
			else:
				return HttpResponse(form.errors, status=404)
		else:
			return HttpResponse(form.errors, status=404)


class UpdateProfile(ListView):
	def get(self,request):
		if request.user.is_anonymous:
			return redirect('account:login')

		profile = Profile.objects.filter(user=request.user)
		form = ProfileForm(instance=request.user.profile)

		return render(request,'account/update_profile.html', {'profile':profile[0],
															'form':form})

	def post(self,request):
		form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('blog:profile', request.user)
		else:
			return HttpResponse(form.errors, status=404)

class UpdatePassword(ListView):
	def get(self,request):
		form = PasswordChangeForm(request.user)
		return render(request, 'account/update_password.html', {'form':form})

	def post(self,request):
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			messages.success(request, '성공적으로 패스워드를 변경 했습니다')
			return redirect('blog:profile',request.user)
		else:
			messages.error(request, 'Please correct the error below')
			return HttpResponse(form.errors, status=404)
