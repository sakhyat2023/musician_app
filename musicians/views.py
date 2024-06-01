from django.shortcuts import render, redirect
from musicians.forms import MusicianForm
from musicians.models import MusicianModel


# Create your views here.
def add_musician(req):
    if req.method == "POST":
        add_form = MusicianForm(req.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect("add_album")
    else:
        add_form = MusicianForm()
    return render(req, "add_musician.html", {"form": add_form})


def edit_musician(req, id):
    data = MusicianModel.objects.get(pk=id)
    if req.method == "POST":
        musician_form = MusicianForm(req.POST, instance=data)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("home")
    else:
        musician_form = MusicianForm(instance=data)
    return render(req, "edit_musician.html", {"form": musician_form})
