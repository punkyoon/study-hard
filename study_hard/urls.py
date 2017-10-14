from django.conf.urls import url, include
from django.contrib import admin

from study_hard.views import main_view


urlpatterns = [
    url(r'^$', main_view, name='main'),
    url(r'^service_main/', include('service_main.urls')),
    url(
        r'^service_admin/([a-zA-Z]{3,}-[a-zA-Z]{3,}-[0-9]{1,4})/',
        include('service_admin.urls')
    ),
    url(
        r'^([a-zA-Z]{3,}-[a-zA-Z]{3,}-[0-9]{1,4})/',
        include('service_study.urls')
    ),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
]
