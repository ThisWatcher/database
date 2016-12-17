from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Artist
from .models import Album
from .models import Albumtracks
from .models import Members
from .models import Singles

def index(request):
    latest_Artist_list = Artist.objects.order_by('id')[:5]
    context = {'latest_Artist_list': latest_Artist_list,}
    return render(request, 'polls/index.html', context)


def detail(request, Artist_id):
    global Artist
    artist = get_object_or_404(Artist, pk=Artist_id)         #kazkodel mazoji
    return render(request, 'polls/detail.html', {'Artist': artist}) #kazkodel mazoji

def albumas(request, Album_id):
    global Album
    album = get_object_or_404(Album, pk=Album_id)
    return render(request, 'polls/albumas.html', {'Album': album})

def members(request,Members_id):
    Member = get_object_or_404(Members, pk=Members_id)         #kazkodel mazoji
    return render(request, 'polls/members.html', {'Member': Member}) #kazkodel mazoji

def single(request,Singles_id):
    global Singles
    single = get_object_or_404(Singles, pk=Singles_id)         #kazkodel mazoji
    return render(request, 'polls/singles.html', {'single': single}) #kazkodel mazoji
