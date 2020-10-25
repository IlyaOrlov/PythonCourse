"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coolapp.urls')),           # ссылка на наш 'coolapp.urls' если просто адр серв то
    path('coolapp/',include('coolapp.urls')),    # :8000 или :8000/coolapp, т.к. в coolapp/urls
                                                 # :8000/2 или :8000/coolapp/2,
                                                 # ''=>'index'  '2'=>'index2'
                                                 # 'coolapp/','coolapp.views.index'
                                                 # 'coolapp/2','coolapp.views.index2'
]
