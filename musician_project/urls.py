
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("musician_home_app.urls")),
    path('musician/', include("musicians.urls")),
    path('album/', include("album.urls")),
]
