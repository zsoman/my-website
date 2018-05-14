from rest_framework.routers import DefaultRouter

from .views import YoutubeVideoViewSet, YoutubePlaylistViewSet

router = DefaultRouter()
router.register(r'youtube/video', YoutubeVideoViewSet, base_name='youtube-video')
router.register(r'youtube/playlist', YoutubePlaylistViewSet, base_name='youtube-playlist')
urlpatterns = router.urls
