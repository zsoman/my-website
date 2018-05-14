from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.documentation import include_docs_urls

api_patterns = [
    url(r'^docs/', include_docs_urls(title='Documentation')),
    
    url(r'^', include(('my_website.apps.youtube_download.urls', 'youtube_download'), namespace='youtube_download')),
]

urlpatterns = [
    url(r'^api/auth/', include('django.contrib.auth.urls')),
    url(r'^api/rest-auth/', include(('rest_auth.urls', 'youtube_download'), namespace='rest_auth')),
    url(r'^api/rest-auth/registration/', include(('rest_auth.registration.urls', 'youtube_download'), namespace='rest_auth_registration')),

    # Allauth
    url(r'^api/accounts/', include('allauth.urls')),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^api/', include((api_patterns, 'youtube_download'), namespace='api')),
    url(r'^api/admin/', admin.site.urls),
]
