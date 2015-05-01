from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PathologyLabProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^labmanagement/', include('labmanagement.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('tokenapi.urls')),
    
)
