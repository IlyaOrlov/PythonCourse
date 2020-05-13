from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^films/$', views.FilmListView.as_view(), name='films'),
    url(r'^film/(?P<pk>\d+)$', views.FilmDetailView.as_view(), name='film-detail'),
    url(r'^directors/$', views.DirectorListView.as_view(), name='directors'),
    url(r'^director/(?P<pk>\d+)$', views.DirectorDetailView.as_view(), name='director-detail'),
]
