from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.files, name='list_files'), #specifies the URL for the view_files application

]
