from django.contrib.auth.models import User
from django.db import models


class DisplayItem(models.Model):
    item_name = models.CharField(max_length=40, unique=True)
    url = models.URLField()
    is_public = models.BooleanField(default=True)


class SlideShow(models.Model):
    show_name = models.CharField(max_length=40, unique=True)
    owner = models.ForeignKey(User)
    display_items = models.ManyToManyField(DisplayItem, through="ShowItems")


class ShowItems(models.Model):
    slide_show = models.ForeignKey(SlideShow)
    display_item = models.ForeignKey(DisplayItem)
    order = models.IntegerField()
