from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoLearn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^index/$', 'blog.views.index'),
    url(r'^index1/$', 'blog.views.index1'),
    url(r'^index2/$', 'blog.views.index2'),
    
    url(r'^blog/register/$', 'blog.views.register'),
    
    url(r'^online/register/$', 'online.views.register'),
    url(r'^online/login/$', 'online.views.login'),
    url(r'^online/index/$', 'online.views.index'),
    url(r'^online/logout/$', 'online.views.logout'),
    
    
    url(r'^online2/login/$', 'online2.views.login'),
    url(r'^online2/index/$', 'online2.views.index'),
    url(r'^online2/logout/$', 'online2.views.logout'),
)