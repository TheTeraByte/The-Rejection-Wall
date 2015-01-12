from django.conf.urls import patterns, url
from post_it_gen import views

# This is the file where URLs are matched with views using regular expression. 
# @author Tushar Bhargava

urlpatterns = patterns('',
    # This regular expression matches to the homepage 
    url(r'^$', views.the_wall, name='home_page'),
    url(r'^submit/',views.submit, name="submit"),
)
