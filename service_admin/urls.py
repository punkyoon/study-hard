from django.conf.urls import url

from service_admin import views


urlpatterns = [
    url(r'^$', views.study_admin_main, name='service_admin'),
    url(
        r'^approve/([a-zA-Z0-9]+)/$',
        views.approve_join_request,
        name='approve_join'
    ),
    url(
        r'^reject/([a-zA-Z0-9]+)/$',
        views.reject_join_request,
        name='reject_join'
    ),
    url(
        r'^manage_deposit/([a-zA-Z0-9]+)/$',
        views.manage_deposit,
        name='manage_deposit'
    ),
    url(
        r'^kickout_member/([a-zA-Z0-9]+)/$',
        views.kickout_member,
        name='kickout_member'
    ),
    url(
        r'^manage_attendance/([a-zA-Z0-9]+)/(attend|late|absent)/$',
        views.manage_attendance,
        name='manage_attendance'
    ),
    url(r'^remove_study/$', views.remove_study, name='remove_study'),
]
