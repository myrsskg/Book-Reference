#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
    url(r'^$', VBRs.as_view(), name='vbr'),
    url(r'^(?P<pk>\d+)/$', VBRedit.as_view()),
    url(r'^add/$', VBRadd.as_view()),
    url(r'^(?P<pk>\d+)/del/$', VBRdel.as_view(), name='vbr_del'),

)
