from django.conf.urls import url
from test.views import login_user, logout_user, register, index
from upload.views import upload
from . import views
from resultspage.views import files



app_name = 'test'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),


]
