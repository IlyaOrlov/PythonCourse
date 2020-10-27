from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from coolapp.models import Film, Commentary
from coolapp.forms import FilmForm, CommentaryForm
from .forms import UserForm
from django.urls import reverse
from django.http.response import HttpResponseNotFound


def main_page(request):
    return render(request, 'coolsite/main_page.html', {'sitename': 'COOL SITE', "user": request.user})


def sign_up(request):
    if request.user.is_authenticated:
        return render(request, 'coolsite/forbidden.html', {"message": "In order to sign up You must to log out"})

    if request.method == "POST":
        form = UserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password']).save()
            return redirect(reverse('main_page'))

    return render(request, 'coolsite/sign_up.html', {"form": UserForm()})


def check_auth(func):
    def wrapper(*args, **kwargs):
        if not args[0].user.is_authenticated:
            return redirect(reverse('main_page'))
        return func(*args, **kwargs)
    return wrapper


@check_auth
def list_films(request):
    films = Film.objects.all()
    return render(request, 'coolsite/films.html', {"films": films, "user": request.user})


@check_auth
def get_film(request, film_id=0):
    film = Film.objects.filter(id=film_id)
    if film:
        film = film[0]
    else:
        return HttpResponseNotFound("The Film not found")

    if request.method == "POST":
        comment = Commentary(film=film,
                             author=request.user.get_username())
        form = CommentaryForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()

    comments = Commentary.objects.filter(film=film)
    content = {"film": film, "comments": comments, "form": CommentaryForm(), "user": request.user}
    return render(request, 'coolsite/film.html', content)


@check_auth
def new_film(request):
    if not request.user.is_staff:
        return render(request, 'coolsite/forbidden.html', {"message": "You cannot edit the site's content"})
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            film = form.save()
            return redirect(reverse('get_film', args=(film.id,)))
    else:
        return render(request, 'coolsite/new_film.html', {'form': FilmForm()})
