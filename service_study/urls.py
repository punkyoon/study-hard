from django.conf.urls import url

from service_study import views


urlpatterns = [
    url(r'^$', views.study_main, name='study_main'),
    url(r'^notice/$', views.list_notice, name='notice'),
    url(r'^fine/$', views.list_fine, name='fine'),
    url(r'^user/([a-zA-Z0-9]+)/$', views.study_user_info, name='user_info'),
    url(r'^exit/([a-zA-Z0-9]+)/$', views.exit_study, name='exit_study'),
    url(r'^info/$', views.study_info, name='study_info'),
    url(r'^paid_fine/([a-zA-Z0-9]+)/$', views.paid_fine, name='paid_fine'),
    url(
        r'^remove_fine/([a-zA-Z0-9]+)/$',
        views.remove_fine,
        name='remove_fine'
    ),
]
