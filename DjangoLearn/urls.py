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
    url(r'^blog/init/$', 'blog.views.bloginit'),
    
    url(r'^online/register/$', 'online.views.register'),
    url(r'^online/login/$', 'online.views.login'),
    url(r'^online/index/$', 'online.views.index'),
    url(r'^online/logout/$', 'online.views.logout'),
    
    
    url(r'^online2/login/$', 'online2.views.login'),
    url(r'^online2/index/$', 'online2.views.index'),
    url(r'^online2/logout/$', 'online2.views.logout'),

    url(r'^model/$', 'blog.views.model'),
    url(r'^model2/$', 'blog.views.model2'),
    url(r'^model3/$', 'blog.views.model3'),
    url(r'^modelall/$', 'blog.views.modelAll'),
    
    
    #url(r'^blog/index/(?P<id>\d{2})/$', 'blog.views.index'),
    
    url(r'^user/init/$', 'django_user.views.init'),
    url(r'^user/login/$', 'django_user.views.login_v'),
    url(r'^user/logout/$', 'django_user.views.logout_v'),
    url(r'^user/$', 'django_user.views.index'),


    url(r'^mf/author$', 'model_form.views.author'),
    url(r'^mf/book$', 'model_form.views.book'),
    url(r'^mf/view_author$', 'model_form.views.view_author'),
    url(r'^mf/view_book$', 'model_form.views.view_book'),
)