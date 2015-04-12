from django.db import models

# Create your models here.
class Video(models.Model):
    instructor = models.ForeignKey('dataCollections.Instructor', related_name='video')
    video_master = models.FileField(upload_to='master_videos')
    video_transcoded = models.BooleanField(default=False)
    video_transcoding = models.BooleanField(default=False)
    transcode_job_id = models.IntegerField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    video_thumbnail_url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return "Instructor " + self.instructor + " Video " + self.video_master.name