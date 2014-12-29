from django.db import models
import random

# Create your models here.

# Almost like a constructor for the model
class PostItManager(models.Manager):
    def create_post_it(self):
        post_it=self.create()
        post_it.random_color_gen()
        return post_it

class PostIt(models.Model):
    content=models.CharField(max_length=400)
    color=models.CharField(max_length=200)
    objects=PostItManager()

    # This function randomly generates a color for the post it note (hexadecimal color code which we can feed to HTML)
    def random_color_gen(self):
        rand=lambda: random.randint(0,255)
        self.color='#%02X%02X%02X' % (rand(),rand(),rand())

    def set_content(self,content_val):
        self.content=content_val

    def __unicode__(self):
        return self.content

