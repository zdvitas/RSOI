from django.conf.urls import patterns, include, url
from django.contrib import admin
import Lab1.urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RSOI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('Lab1.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
