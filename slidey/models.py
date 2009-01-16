from django.db import models


class DisplayItem(models.Model):
    item_name = models.CharField(max_length=40, unique=True)
    url = models.URLField()
    is_public = models.BooleanField(default=True)


class SlideShow(models.Model):
    show_name = models.CharField(max_length=40, unique=True)
