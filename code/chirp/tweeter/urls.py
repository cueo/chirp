from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^auth/$', views.auth, name="auth"),
    url(r'^(?P<handle>[a-zA-Z_]+)/$', views.user_profile, name="profile"),
    url(r'^(?P<handle>[a-zA-Z_]+)/following/$', views.following, name="following"),
    url(r'^(?P<handle>[a-zA-Z_]+)/followers/$', views.followers, name="followers"),
	url(r'^registration/success.html$', views.registration_success, name="registration_success"),
	url(r'^registration/', views.registration, name="registration")
]
