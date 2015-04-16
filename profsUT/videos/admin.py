import traceback

from django.contrib import admin
from django.contrib import messages
from django.core.urlresolvers import reverse

from models import *
import views

from profsUT import settings

from heywatch import job

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    actions = ('transcode',)
    include = ('instructor', 'video_master',)

    def transcode(self, request, queryset):
        for video in queryset:
            if video.video_transcoded:
                messages.error(request, "Video for %s already transcoded" % video.instructor)
                continue
            if video.video_transcoding:
                messages.error(request, "Video for %s is transcoding already" % video.instructor)
                continue
            
            heywatch_conf = []

            # the way I'm building our urls is kind of sloppy. Ideally we'd 
            # handle this all through Django's url system. Need to refactor
            # when there is time
            heywatch_conf.append("".join(("var s3 = s3://", 
                                          settings.AWS_ACCESS_KEY_ID,
                                          ":",
                                          settings.AWS_SECRET_ACCESS_KEY,
                                          "@", 
                                          settings.AWS_STORAGE_BUCKET_NAME,
                                          "/video",
                                          )))
            heywatch_conf.append("".join(("set source = ",
                                          video.video_master.url,
                                          )))
            heywatch_conf.append("".join(("set webhook = ",
                                          request.build_absolute_uri(reverse('videos:heyWatchHook')),
                                          )))
            heywatch_conf.append("".join(("-> hls = ", 
                                          "$s3/hls/",
                                          str(video.id),
                                          ".m3u8"
                                          )))
            heywatch_conf.append("".join(("-> jpg_640x = ",
                                          "$s3/thumbnail/large/",
                                          str(video.id),
                                          "_#num#.jpg, number=1"
                                          )))

            heywatch_conf = "\n".join(heywatch_conf)
            
            try:
                response = job.submit(heywatch_conf, api_key=settings.VIDEOS_ZENCODER_KEY)
            except:
                trace = traceback.format_exc()
                messages.error(request, "Exception encountered while submitting the video for processing: %s" % trace)
                continue

            if response['status'] != 'ok':
                messages.error(request, "Transcode request failed: %s" % str(response))
                continue

            video.video_transcoding = True
            video.transcode_job_id = int(response['id'])
            video.save()
            messages.success(request, 'Video submitted for transcoding')

admin.site.register(Video, VideoAdmin)