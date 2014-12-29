from django.conf.urls import patterns, include, url
from post_it_gen import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'the_rejection_wall.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('post_it_gen.urls',namespace="post_it_gen")),
)
