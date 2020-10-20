"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import main_page, list_films, get_film, new_film, sign_up

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', sign_up, name="sign_up"),
    path('login/', LoginView.as_view(template_name='coolsite/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('coolapp/', include('coolapp.urls')),
    path('new/', new_film, name='new_film'),
    path('films/', list_films, name='list_films'),
    path('films/<int:film_id>/', get_film, name='get_film'),
    path('', main_page, name='main_page'),
]
