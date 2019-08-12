from django.contrib.staticfiles.views import serve
from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [

path('', views.index, name='index'),
path('index.html', views.index, name='index'),
path('post.html', views.post),
path('about.html', views.about),
path('contact.html', views.contact),

]
