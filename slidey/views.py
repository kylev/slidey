from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader

from slideshow.slidey.models import SlideShow

def index(request):
    t = loader.get_template('index.html')
    all_shows = SlideShow.objects.all()
    return render_to_response('index.html', {'show_list': all_shows})


def show(request, show_id):
    return HttpResponse("Show %s." % (show_id,))
