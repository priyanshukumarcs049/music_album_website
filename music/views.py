from .models import Album
from django.shortcuts import render
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Does Not Exist")
    return render(request, 'music/detail.html', {'album': album})
