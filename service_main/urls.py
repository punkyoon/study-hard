from django.conf.urls import url, include
from django.contrib import admin

from service_main import views


urlpatterns = [
    url(r'^$', views.list_study, name='study_list'),
    url(r'^create/$', views.create_study, name='create_study'),
]