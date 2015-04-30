from rest_framework import serializers

from videos.models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('video_url', 'video_thumbnail_url')

class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Video
        fields = ('video_url', 'video_thumbnail_url', 'instructor')