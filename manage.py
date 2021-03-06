#!/usr/bin/env python

# to run the server:
# python manage.py runserver

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cms.settings_dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
