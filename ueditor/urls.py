#coding=utf-8
'''
Created on 2012-9-3

@author: 王健
'''
from django.conf.urls import patterns, include, url

from ueditor.views import imageUp, fileUp, getRemoteImage, imageManager, getMovie


urlpatterns = patterns('^ueditor/$',
    (r'^imageUp$',imageUp ),#
    (r'^fileUp$',fileUp ),#
    (r'^getRemoteImage',getRemoteImage ),#
    (r'^imageManager',imageManager ),#
    (r'^getMovie',getMovie ),#

)