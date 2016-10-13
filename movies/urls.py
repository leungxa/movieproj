from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.movie_info, name='movie_info'),
    url(r'^search/', views.search, name='search'),
]