from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^slideshow/', include('slidey.slideshow.urls')),
    # Admin is currently enabled.
    (r'^admin/(.*)', admin.site.root),
)
