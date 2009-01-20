import os

from django.conf.urls.defaults import *


APP_DIR = os.path.dirname(os.path.normpath(__file__))


urlpatterns = patterns(
    'slideshow.slidey.views',
    (r'^$', 'index'),
    (r'^static/(?P<path>.*)$', 'static', None, 'slidey-static'),
    (r'(?P<show_id>\d+)/$', 'show'),
    (r'^login/$', 'do_login', None, 'slidey-login'),
    (r'^manage/$', 'manage', None, 'slidey-manage'),
    )
