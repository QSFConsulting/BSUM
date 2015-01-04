#!/bin/bash
echo "Did you change manage.py settings into production settings?"
scp ~/BSUM/manage.py root@104.236.117.61:/home/django/django_project/manage.py
scp -r ~/BSUM/cms root@104.236.117.61:/home/django/django_project/
