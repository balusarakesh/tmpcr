from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^date$', views.date, name='date'),
    url(r'^create$', views.create, name='create'),
    url(r'^delete/\d+$', views.delete, name='delete'),
]