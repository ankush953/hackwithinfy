from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from frame.views import homepage, searchbycat

urlpatterns = [
    path('', homepage,name='home'),
    path('search/<str:cat>/',searchbycat,name='searchtype'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
