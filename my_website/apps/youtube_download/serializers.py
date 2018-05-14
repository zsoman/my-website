from rest_framework.serializers import ModelSerializer

from .models import YoutubeVideo, YoutubePlaylist


class YoutubeVideoSerializer(ModelSerializer):
    class Meta:
        queryset = YoutubeVideo.objects.all()
        model = YoutubeVideo
        fields = ('id', 'url_id', 'title', 'video_id')


class YoutubePlaylistSerializer(ModelSerializer):
    class Meta:
        queryset = YoutubePlaylist.objects.all()
        model = YoutubePlaylist
        fields = ('id', 'playlist_id', 'title', 'videos')
