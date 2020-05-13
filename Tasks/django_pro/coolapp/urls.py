from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('films', views.films, name='films'),
    path('new', views.new, name='new'),
    path('<int:film_id>/', views.new, name='new'),
]
