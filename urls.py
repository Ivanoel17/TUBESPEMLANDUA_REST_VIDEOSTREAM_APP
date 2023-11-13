# videostream_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet
from .views import video_list, upload_video

router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='video')

urlpatterns = [
    path('videos/', video_list, name='video-list'),
    path('upload/', upload_video, name='upload-video'),
    path('', include(router.urls)),
]
