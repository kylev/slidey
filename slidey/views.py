import os

import django.views.static
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader

from slideshow.slidey.models import SlideShow


def index(request, form=None):
    if not form:
        form = AuthenticationForm()

    all_shows = SlideShow.objects.all()
    return render_to_response('index.html', {'show_list': all_shows,
                                             'form': form})


STATIC_ROOT = os.path.dirname(os.path.normpath(__file__)) + '/static'

def static(request, path):
    """Return app-relative static resources and collateral."""
    return django.views.static.serve(request, path, STATIC_ROOT)


def show(request, show_id):
    """TODO Display a slide show."""
    return render_to_response('show_frameset.html', {'show_id': show_id})


def show_control(request, show_id):
    slides = SlideShow.objects.get(id=show_id).display_items.all()
    return render_to_response('show_control.html', {'slides': slides})


def do_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('slidey-manage'))
    else:
        form = AuthenticationForm(request)

    return index(request, form=form)


@login_required
def manage(request):
    my_shows = SlideShow.objects.filter(owner=request.user)

    return render_to_response('manage.html', {'show_list': my_shows})


def show_contents(request, show_id):
    """Return a JSON description of the elements in a show."""
    slides = SlideShow.objects.get(id=show_id).display_items.all()
    return HttpResponse(serialize('json', slides), mimetype='application/json')


@login_required
def edit(request, show_id):
    slides = SlideShow.objects.get(id=show_id).display_items.all()

    return render_to_response('edit_show.html', {'slide_list': slides})

