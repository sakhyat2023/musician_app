from django.db import models
from musicians.models import MusicianModel


# Create your models here.
class AlbumModel(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE, default=None)
    release_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")], default=3
    )

    def __str__(self):
        return self.album_name
