from django.conf.urls import url

from service_study import views


urlpatterns = [
    url(r'^$', views.study_main, name='study_main'),
    url(r'^notice/$', views.list_notice, name='notice'),
    url(r'^user/([a-zA-Z]+)/$', views.study_user_info, name='user_info'),
    url(r'^info/$', views.study_info, name='study_info'),
]