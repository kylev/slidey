import os

import django.views.static
from django.conf.urls.defaults import *
from django.core.urlresolvers import RegexURLPattern


APP_DIR = os.path.dirname(os.path.normpath(__file__))

urlpatterns = patterns(
    'slideshow.slidey.views',
    (r'^$', 'index'),
    # Annoying hack to serve static content from this app dir
    RegexURLPattern(r'^static/(?P<path>.*)$', django.views.static.serve,
                    {'document_root': APP_DIR + '/static'}, 'slidey-static'),
    (r'(?P<show_id>\d+)/$', 'show'),
    )
