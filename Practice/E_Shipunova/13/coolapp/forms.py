from django import forms
from .models import Film
from .models import Comment


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'desc', 'rate')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comm',)
