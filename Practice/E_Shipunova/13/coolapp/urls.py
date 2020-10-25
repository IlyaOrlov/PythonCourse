from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('premieres', views.premieres, name='premieres'),
    path('films', views.films, name='films'),
    path('new', views.new, name='new'),
    path('<int:film_id>/', views.new, name='new'),
    url(r'^films/(?P<question_id>\d+)$', views.detail, name='detail'),
]
