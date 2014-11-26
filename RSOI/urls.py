from django.conf.urls import patterns, include, url
from django.contrib import admin
import Lab1.urls
urlpatterns = patterns('',
    # Examples:
    url(r'^', include('Lab1.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
