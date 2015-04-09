from django.db import models

# Create your models here.
class Video(models.Model):
    instructor = models.ForeignKey('dataCollections.Instructor')
    video_master = models.FileField(upload_to='master_videos')
    video_transcoded = models.BooleanField()
    video_transcoding = models.BooleanField()
    transcode_job_id = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return "Instructor %s Video %s" % instructor, video_master.name