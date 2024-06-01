from django.shortcuts import render
from album.models import AlbumModel

# Create your views here.
def home_page(req):
    posts = AlbumModel.objects.all()
    return render(req, "index.html", {"posts": posts})