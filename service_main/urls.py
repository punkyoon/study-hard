from django.conf.urls import url

from service_main import views


urlpatterns = [
    url(r'^$', views.list_study, name='study_list'),
    url(r'^create/$', views.create_study, name='create_study'),
    url(
        r'^join_request/([a-zA-Z]{3,}-[a-zA-Z]{3,}-[0-9]{1,4})/$',
        views.join_request_study,
        name='join_request'
    ),
    url(r'^my_study/$', views.my_study, name='my_study'),
]