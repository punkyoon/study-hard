from django.conf.urls import url

from service_main import views


urlpatterns = [
    url(r'^$', views.list_study, name='study_list'),
    url(r'^create/$', views.create_study, name='create_study'),
    url(r'^my_study/$', views.my_study, name='my_study'),
]