from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add_new, name='add'),
    url(r'^view/(?P<id>\d+)$', views.view, name='view'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    url(r'^uploadfile$', views.uploadfile, name='uploadfile'),
]
