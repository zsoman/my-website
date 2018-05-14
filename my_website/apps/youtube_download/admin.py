from django.contrib import admin

from .models import YoutubeVideo, YoutubePlaylist

admin.site.register(YoutubeVideo)
admin.site.register(YoutubePlaylist)