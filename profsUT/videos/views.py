from django.shortcuts import render

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from models import Video

import json
import logging
import traceback

logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
@require_POST
def heyWatchPost(request):
    try:
        response = json.loads(request.body)
        video = Video.objects.get(transcode_job_id=int(response['id']))
        video.video_transcoding = False
        video.transcode_job_id = None
        if len(response['errors']) != 0:
            logger.error('Error in response for video transcoding job of %s: %s' % (video.instructor, str(response)))
        else:
            video.video_thumbnail_url = response['output_urls']['jpg_640x'][0]
            video.video_url = response['output_urls']['hls']
            video.video_transcoded = True
            logger.info('Success for video transcoding job of %s: %s' % (video.instructor, str(response)))
        
        video.save()
    except:
        logger.error('Everything sucks, and your heywatchpost has an uncaught exception: %s' % traceback.format_exc())
        raise
    return HttpResponse("")