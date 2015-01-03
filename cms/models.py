#from django.conf import settings
from django.db import models
#from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class News(models.Model):

    override_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    content = models.TextField()
    headline = models.CharField(max_length=140)

    def __unicode__(self):
        if len(self.headline) > 20:
            return self.headline[:17] + "..."
        else:
            return self.headline

    class Meta:
        verbose_name = "Piece of news"
        verbose_name_plural = "News"
