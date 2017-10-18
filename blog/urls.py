from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views as blog_view

app_name = 'blog'

urlpatterns = [
	url(r'^$', blog_view.Index.as_view(), name='index'),	
	url(r'^profile/(?P<user>\w+)/$', blog_view.MyProfile.as_view(), name='profile'),
	url(r'^post/(?P<tag>[\w|\W]+)/$', blog_view.SearchingTag.as_view(), name='searchingtag'),
	url(r'^place/(?P<qlocation>[\w|\W]+)/$', blog_view.SearchingLocation.as_view(), name='searchinglocation'),
	url(r'^remove/(?P<pk>\d+)/$',blog_view.RemovePost.as_view(), name='removepost'),
	url(r'^mod/(?P<pk>\d+)/$',blog_view.ModifyPost.as_view(), name='modifypost'),
	url(r'^searching/$',blog_view.Searching.as_view(),name='searching'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
