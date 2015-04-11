from django.shortcuts import render

from django.views.decorators.http import require_POST

from models import Video

import json
import logging

logger = logging.getLogger(__name__)
# Create your views here.

@require_POST()
def heyWatchPost(request, transcode_id):
    video = Videos.object.get(transcode_job_id=transcode_id)
    response = json.loads(request.body)
    video.video_transcoding = False
    video.transcode_job_id = None
    if 'errors' in response:
        logger.error('Error in response for video transcoding job of %s: %s' % video.instructor, str(response))
    else:
        video.video_thumbnail_url = respone['jpg_640x']
        video.video_url = response['hls']
        video.video_transcoded = True
    
    video.save()