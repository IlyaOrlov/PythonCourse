from django import forms
from .models import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('name', 'desc', 'rate')
# поля pub_date и id заполняются сами
