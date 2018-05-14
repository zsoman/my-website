from django.db import models
from . import YOUTUBE_URI


class YoutubeVideo(models.Model):
    url_id = models.CharField(max_length=512)
    title = models.CharField(max_length=512)
    video_id = models.CharField(max_length=512)

    def full_url(self):
        return '{}{}'.format(YOUTUBE_URI, self.url_id)

    def __str__(self):
        return '{} ( {} ) '.format(self.title.encode('utf-8'), self.full_url())


class YoutubePlaylist(models.Model):
    playlist_id = models.CharField(max_length=512)
    title = models.CharField(max_length=512)
    videos = models.ForeignKey(YoutubeVideo, related_name='playlist', on_delete=models.CASCADE)

    def __str__(self):
        return '{} ({}) - {}'.format(self.title, len(self.videos), self.playlist_id)
