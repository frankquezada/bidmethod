from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^signup', views.SignUp.as_view(), name='signup'),
]