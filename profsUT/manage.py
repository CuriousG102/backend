#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "profsUT.settings")

    from django.core.management import execute_from_command_line

    print "POODLES" + sys.path

    execute_from_command_line(sys.argv)
