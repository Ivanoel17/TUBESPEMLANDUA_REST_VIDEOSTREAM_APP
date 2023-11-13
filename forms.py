# videostream_app/forms.py

from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']

    video_file = forms.FileField(widget=forms.FileInput(attrs={'accept': 'video/*'}))
