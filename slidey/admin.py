from django.contrib import admin

import slideshow.slidey.models

admin.site.register(slideshow.slidey.models.SlideShow)
admin.site.register(slideshow.slidey.models.DisplayItem)

