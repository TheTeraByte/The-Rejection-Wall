from django.conf.urls import patterns, include, url
from post_it_gen import views
from django.contrib import admin
admin.autodiscover()

# In this file we simply include the URL handlers defined in the 'post-it' sub-app.

urlpatterns = patterns('',
   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('post_it_gen.urls',namespace="post_it_gen")),
)
