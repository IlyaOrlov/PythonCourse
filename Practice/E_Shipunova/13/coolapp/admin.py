from django.contrib import admin
from .models import Film
from .models import Comment

admin.site.register(Film)
admin.site.register(Comment)
