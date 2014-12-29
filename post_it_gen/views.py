from django.shortcuts import render
from django.http import HttpResponse
from post_it_gen.models import PostIt,PostItManager
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

# The main view that shows the rejection wall 
def the_wall(request):
    # Creating a 'context' which is basically this bundle of python that we link with the webpage to give it turbo powers
    all_rejections=PostIt.objects.all()
    context={'all_rejections':all_rejections}
    # Returning an HttpResponse object which is a webpage linked with a context. 
    return render(request,'post_it_gen/index.html',context)

# This view handles submitting the post it text. 
def submit(request):
      
    entered_content=request.POST['text_input_bar']
    # I'm not sure whether this is creating the post it but worth a shot.
    post_it=PostIt.objects.create_post_it()
    # Setting the content for the post-it
    post_it.set_content(entered_content)
    # Saving the post-it to the database
    post_it.save()
    return HttpResponseRedirect(reverse('post_it_gen:home_page'))

