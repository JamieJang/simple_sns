from django.conf.urls import url
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name='account'

urlpatterns = [
	url(r'^signup/$', views.my_signup.as_view(), name='signup'),
	url(r'^login/$', views.my_login.as_view(), name='login'),
	url(r'^logout/$', auth_view.logout, {'next_page':'blog:index'}, name='logout'),

	url(r'^update/$', views.UpdateProfile.as_view(), name='update'),
	url(r'^update/password/$', views.UpdatePassword.as_view(), name='update_password'),
] 

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)