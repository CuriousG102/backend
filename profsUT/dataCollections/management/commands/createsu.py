import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username=os.environ["DEFAULT_ADMIN_USER"]).exists():
            User.objects.create_superuser(os.environ["DEFAULT_ADMIN_USER"], 
                                          "profsut@gmail.com", 
                                          os.environ["DEFAULT_ADMIN_PASS"])