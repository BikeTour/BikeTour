from django.conf.urls import patterns, include, url
from cicloponto import views

urlpatterns = patterns('',
    url(r'^$', views.view_index, name='index'),
)
