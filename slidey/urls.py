from django.conf.urls.defaults import *


urlpatterns = patterns(
    'slideshow.slidey.views',
    (r'^$', 'index'),
    # TODO static serve
    #(r'site_media/(?P<path>.*)$', 'django.views.static.serve',
    # {
    (r'(?P<show_id>\d+)/$', 'show'),
    )
