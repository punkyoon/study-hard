from django.conf.urls import url

from service_study import views


urlpatterns = [
    url(r'^$', views.study_main, name='study_main'),
    url(r'^notice/$', views.list_notice, name='notice'),
]