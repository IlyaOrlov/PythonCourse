from django.shortcuts import render
from .models import Film, Director, Genre
from django.views import generic


def index(request):
    num_films = Film.objects.all().count()
    num_directors = Director.objects.all().count()
    num_genres = Genre.objects.all().count()
    return render(request, 'coolapp/index.html',
                  context={'num_films': num_films, 'num_directors': num_directors, 'num_genres': num_genres}, )


class FilmListView(generic.ListView):
    model = Film


class FilmDetailView(generic.DetailView):
    model = Film


class DirectorListView(generic.ListView):
    model = Director


class DirectorDetailView(generic.DetailView):
    model = Director
