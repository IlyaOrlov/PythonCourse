from django.contrib import admin
from .models import Film, Genre, Director


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'display_genre')
    list_filter = ('director', 'genre')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
