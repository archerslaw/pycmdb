from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simplecmdb.views.home', name='home'),
    # url(r'^simplecmdb/', include('simplecmdb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^api/collect$', 'hostinfo.views.collect'),
    url(r'^api/gethostbyident$', 'hostinfo.views.getHostByIdentity'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/gethosts\.json$', 'hostinfo.views.gethostsjson'),
    url(r'^api/gethosts\.txt$', 'hostinfo.views.gethoststxt'),
)
