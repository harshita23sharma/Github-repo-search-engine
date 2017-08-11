from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^your-name/$', views.name , name='name'),
    url(r'^your-name/selected-result/', views.selected , name='selected'),
    url(r'^your-name/selected-result/results/', views.results , name='results'),

    
]