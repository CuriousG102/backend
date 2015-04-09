from django.shortcuts import render

from django.views.decorators.http import require_POST
# Create your views here.

@require_POST()
def heyWatchPost(request, transcode_id):
