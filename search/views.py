# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

#Process the default request, returns the index page
def index(request):
    return render_to_response('search/index.html',
            context_instance=RequestContext(request))
def results(request):
    return render_to_response('search/results.html',
            context_instance=RequestContext(request))


