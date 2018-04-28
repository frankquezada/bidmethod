from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^my-bids/$', views.MyBids.as_view(), name='my-bids'),
    url(r'^edit-bid/(?P<pk>[0-9]+)/add-documents/$', views.AddDocuments.as_view(), name='add-documents'),
    url(r'^edit-bid/(?P<pk>[0-9]+)/$', views.EditBid.as_view(), name='edit-bid'),
    url(r'^add-bid/$', views.AddBid.as_view(), name='add-bid'),
]