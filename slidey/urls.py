from django.conf.urls.defaults import patterns


urlpatterns = patterns(
    'slideshow.slidey.views',
    (r'^$', 'index'),
    (r'^static/(?P<path>.*)$', 'static', None, 'slidey-static'),
    (r'^(?P<show_id>\d+)/$', 'show'),
    (r'^show_control/(?P<show_id>\d+)/$', 'show_control', None, 'slidey-control'),
    (r'^login/$', 'do_login', None, 'slidey-login'),
    (r'^manage/$', 'manage', None, 'slidey-manage'),
    (r'^show_contents/(?P<show_id>\d+)/$', 'show_contents', None, 'slidey-showcont'),
    (r'^edit/(?P<show_id>\d+)/$', 'edit', None, 'slidey-edit'),
    )
