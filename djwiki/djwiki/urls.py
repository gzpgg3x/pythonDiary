# from django.conf.urls import patterns, include, url

# # Uncomment the next two lines to enable the admin:
# # from django.contrib import admin
# # admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'djwiki.views.home', name='home'),
#     # url(r'^djwiki/', include('djwiki.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     # url(r'^admin/', include(admin.site.urls)),
# )



# from django.conf.urls.defaults import patterns, url

# urlpatterns = patterns('wiki.views',
#     url(r'^$', 'index'),
# )



from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from wiki.views import * #added

urlpatterns = patterns('',
    # url(r'^wiki/', include('djwiki.urls')),
    ('^$', home), #added
    (r'^page/(?P<page_id>\d+)/$',page_specific), #added
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'wiki.views.index'),
)
