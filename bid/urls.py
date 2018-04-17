from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^bid/$', views.Bid.as_view(), name='bid'),
]