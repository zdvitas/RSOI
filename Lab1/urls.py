from django.conf.urls import patterns, url

from Lab1 import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^login', views.login, name='login'),

)
