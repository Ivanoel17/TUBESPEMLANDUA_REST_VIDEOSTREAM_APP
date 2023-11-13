from django.shortcuts import render

# Create your views here.
# videostream_app/views.py
from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videostream_app/video_list.html', {'videos': videos})

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def list(self, request, *args, **kwargs):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        return render(request, 'videostream_app/video_list.html', {'videos': serializer.data})
    
# videostream_app/views.py

from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videostream_app/video_list.html', {'videos': videos})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video-list')
    else:
        form = VideoForm()

    return render(request, 'videostream_app/upload_video.html', {'form': form})
