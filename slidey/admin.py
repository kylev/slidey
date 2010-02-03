from django.contrib import admin

import slidey.slideshow.models

admin.site.register(slidey.slideshow.models.SlideShow)
admin.site.register(slidey.slideshow.models.DisplayItem)

