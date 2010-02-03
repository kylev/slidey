from django.contrib.auth.models import User
from django.db import models


class SlideShow(models.Model):
    show_name = models.CharField(max_length=40, unique=True)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.show_name


class DisplayItem(models.Model):
    slide_show = models.ForeignKey(SlideShow)
    item_name = models.CharField(max_length=40, unique=True)
    url = models.URLField()
    display_duration = models.PositiveIntegerField(default=20)

    def __unicode__(self):
        return "%s (%s)" % (self.item_name, self.url)
