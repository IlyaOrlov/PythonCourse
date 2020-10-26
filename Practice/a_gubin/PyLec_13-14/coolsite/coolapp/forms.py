from django import forms
from .models import Film, Commentary


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'desc', 'rate')


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ('comm',)
