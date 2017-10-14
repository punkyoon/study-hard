from django.conf.urls import url, include
from accounts import views


urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(
        r'^delete_account/$',
        views.delete_account_view,
        name='delete_account'
    ),
    url(
        r'^delete_account_done/$',
        views.delete_account_done_view,
        name='delete_account_done'
    ),
]
