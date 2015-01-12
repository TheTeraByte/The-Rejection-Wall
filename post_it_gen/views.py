from django.shortcuts import render
from django.http import HttpResponse
from post_it_gen.models import PostIt,PostItManager
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# This file stores all 'views' of the Django project. "A view in Python is a function that takes a Web request
# and returns a Web response." ~ From official documentation. 
# @author Tushar Bhargava

# The main view that shows the rejection wall (the home page so to speak) 
def the_wall(request):
    # Creating a 'context' which is basically this bundle of python that we link with the webpage to give it turbo powers.
    all_rejections=PostIt.objects.all()
    # Storing all the rejection post-its in the context
    context={'all_rejections':all_rejections}
    # Returning an HttpResponse object, which is the webpage linked with the context. 
    return render(request,'post_it_gen/index.html',context)

# This view handles submitting the post-it text for storage in the database. 
def submit(request):
    entered_content=request.POST['text_input_bar']
    post_it=PostIt.objects.create_post_it()
    post_it.set_content(entered_content)
    # Saving the post-it to the database
    post_it.save()
    return HttpResponseRedirect(reverse('post_it_gen:home_page'))

