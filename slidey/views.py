from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader

from slideshow.slidey.models import SlideShow

def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
    else:
        form = AuthenticationForm()

    all_shows = SlideShow.objects.all()
    return render_to_response('index.html', {'show_list': all_shows,
                                             'form': form})


def show(request, show_id):
    return HttpResponse("Show %s." % (show_id,))


def login(request):
    #username = request.POST['username']
    #password = request.POST['password']
    #user = authenticate(username=username, password=password)
    form = AuthenticationForm(request.POST)
    form.is_valid()
    user = form.get_user()
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('manage')
        else:
            print "Your account has been disabled!"
    else:
        return index(request)


@login_required
def manage(request):
    return HttpResponse("Running as %s." % (request.user,))
