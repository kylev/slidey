import os

import django.views.static
from django.conf.urls.defaults import *
from django.core.urlresolvers import RegexURLPattern


APP_DIR = os.path.dirname(os.path.normpath(__file__))


urlpatterns = patterns(
    'slideshow.slidey.views',
    (r'^$', 'index'),
    (r'^static/(?P<path>.*)$', 'static', None, 'slidey-static'),
    (r'(?P<show_id>\d+)/$', 'show'),
    (r'^login/$', 'login', None, 'slidey-login'),
    (r'^manage/$', 'manage', None, 'slidey-manage'),
    )
