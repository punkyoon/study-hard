from django.conf.urls import url

from service_admin import views


urlpatterns = [
    url(r'^$', views.study_admin_main, name='service_admin'),
    url(r'^approve/([a-zA-Z]+)/$', views.approve_join_request, name='approve_join'),
    url(r'^reject/([a-zA-Z]+)/$', views.reject_join_request, name='reject_join'),
]