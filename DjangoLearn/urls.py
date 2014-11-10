from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoLearn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', 'blog.views.index'),
    url(r'^index1/$', 'blog.views.index1'),
    url(r'^index2/$', 'blog.views.index2'),
    url(r'^model/$', 'blog.views.model'),
    url(r'^model2/$', 'blog.views.model2'),
    url(r'^model3/$', 'blog.views.model3'),
    url(r'^modelall/$', 'blog.views.modelAll'),
    
    
    #url(r'^blog/index/(?P<id>\d{2})/$', 'blog.views.index'),
    url(r'^blog/init/$', 'blog.views.bloginit'),
    
    url(r'^user/init/$', 'django_user.views.init'),
    url(r'^user/login/$', 'django_user.views.login_v'),
    url(r'^user/logout/$', 'django_user.views.logout_v'),
    url(r'^user/$', 'django_user.views.index'),
)