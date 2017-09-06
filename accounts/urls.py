from django.conf.urls import url, include
from accounts import views


urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),
    url(r'^register/', views.register_view, name='register'),
    url(r'profile/', views.profile_view, name='profile'),
]
