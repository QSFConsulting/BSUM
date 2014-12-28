from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^news/', 'cms.views.get_news'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^static/admin/', include(admin.site.urls)),
)
