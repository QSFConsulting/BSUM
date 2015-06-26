BSUM
====
Biotech Start-Up Management


# Deploying project to the server
## Unix
### Moving files to the server

1. Merge current changes into "Release" branch and switch to it (you will always have 2 branches)
2. Ensure that you've got the production settings on
3. run `deploy.bash`
4. Insert username `root` and password

### Reloading static files and restarting service

1. Take an ssh connection to the host: `ssh root@188.166.28.185`
2. Change to project directory: `cd /home/django/django_project/`
3. Collect updated static files: `python manage.py collectstatic`
4. Restart NGinx static files provider: `sudo service nginx restart`
5. Restart Gunicorn HTTP server: `sudo service gunicorn restart`

You're now done. You can now logout from the server.

_In case there's a problem, you can look for hints at /home/django/readme.txt_