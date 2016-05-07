from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'perfis.views.index'),
    url(r'^login/', 'perfis.views.login'),
)
