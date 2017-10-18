from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls', namespace='blog')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^social/',include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns += [
		url(r'^__debug__/',include(debug_toolbar.urls)),
	]