from django.conf.urls.defaults import *


urlpatterns = patterns(
    'slideshow.slidey.views',
    (r'^$', 'index'),
    (r'(?P<show_id>\d+)/$', 'show'),
    )
