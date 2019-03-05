from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$|^index/$', views.search_list, name='search_list'),
]
