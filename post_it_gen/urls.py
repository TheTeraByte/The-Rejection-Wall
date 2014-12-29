from django.conf.urls import patterns, url
from post_it_gen import views

urlpatterns = patterns('',
    # This regular expression matches to the homepage (at least I think so) 
    url(r'^$', views.the_wall, name='home_page'),
    url(r'^submit/',views.submit, name="submit"),
)
