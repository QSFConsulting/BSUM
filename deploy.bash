#!/bin/bash
echo "Did you change manage.py settings into production settings?"
scp ~/BSUM/manage.py root@188.166.37.173:/home/django/django_project/manage.py
scp -r ~/BSUM/cms root@188.166.37.173:/home/django/django_project/
