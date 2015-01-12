from django.contrib import admin
from post_it_gen.models import PostIt

# Registering my data 'model' i.e. the post-it data storage format with the app.
admin.site.register(PostIt)
