from django.conf.urls.defaults import *
urlpatterns = patterns('search.views',
       (r'^$', 'index'),
       (r'^search$', 'search'),
       (r'^results$', 'results'),
       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
           {'document_root':'/Users/ritesh/code/django_static'}),
)
