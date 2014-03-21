from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import logout
from WJBlog2 import settings
from blog.views import index
from util.imageCode import display
from util.tool import login_blog

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WJBlog2.views.home', name='home'),
    # url(r'^WJBlog2/', include('WJBlog2.foo.urls')),
    (r'^$',index),
    (r'^imagecode$',display),
    (r'^blog/',include('blog.urls')),

    (r'^accounts/login/$',login_blog,{'template_name': 'login.html'}),
    (r'^accounts/logout/$', logout,{'template_name': 'logout.html'}),
    (r'^accounts/profile/$',index),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/', include('ueditor.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),  )
