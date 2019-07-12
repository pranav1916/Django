from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^details/p=(?P<id>\d+)/$', views.details, name='details')
];