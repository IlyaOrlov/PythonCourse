from django.shortcuts import render
from django.http import Http404
from .models import Film
from .forms import FilmForm
from django.shortcuts import redirect
from .models import Comment
from .forms import CommentForm


def main_page(request):

    count_films = Film.objects.all().count()

    return render(
        request,
        'coolapp/main_page.html',
        context={'genres': ['Action movie;', 'Comedy;', 'Sci-fi;', 'Family movie;', 'Silent film;', 'Thriller.'],
                 'count_films': count_films})                 # for use Django language


def premieres(request):
    return render(request, 'coolapp/premieres.html')          # for for new page of site


def films(request):
    return render(request, 'coolapp/films.html', {'films': Film.objects.all()})


def new(request, film_id=None):                                # this function and new.html only for admin

    if not request.user.is_superuser:                          # if user isn't an admin, go to error.html
        return render(request, 'coolapp/error.html')

    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()
            return redirect('/{}'.format(film.id), film=film)

    if film_id:
        film = Film.objects.get(id=film_id)
    else:
        film = Film()

    return render(request, 'coolapp/new.html',
                  {'form': FilmForm(instance=film)})


def detail(request, question_id, comm_id=None):

    try:
        film = Film.objects.get(id=question_id)                  # if no such id exists, throw error
    except Film.DoesNotExist:
        raise Http404("Film does not exist")

    if request.method == 'POST':                                 # 2
        form = CommentForm(request.POST)                         # read form

        if form.is_valid():                                      # check form
            comm = form.save(commit=False)
            comm.film = film                                     # add film
            comm.save()                                          # and save instance

    if not comm_id:                                              # 1 request.method == 'GET'
        comm = Comment()                                         # create empty instance

    return render(request, 'coolapp/detail.html', context={'film': film, 'form': CommentForm(instance=comm)})


