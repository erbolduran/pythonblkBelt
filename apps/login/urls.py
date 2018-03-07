from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^registration$', views.registration),
  url(r'^login$', views.login),
  url(r'^success$', views.success),
  url(r'^success/(?P<number>\d+)$', views.addfriend),
  url(r'^user/(?P<number>\d+)$', views.show),
  url(r'^user/(?P<number>\d+)/unfriend$', views.unfriend),
  url(r'^logout$', views.logout),
]