from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from upload.views import upload
from resultspage.views import files

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', include('test.urls')),
    url(r'^', include('test.urls')),
    url(r'^upload', include('upload.urls')),
    url(r'^files', include('resultspage.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
