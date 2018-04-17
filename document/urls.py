from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^my-documents/$', views.MyDocuments.as_view(), name='my-documents'),
    url(r'^add-document/$', views.AddDocument.as_view(), name='add-document'),
    url(r'^edit-document/(?P<pk>[0-9]+)/$', views.EditDocument.as_view(), name='edit-document'),
]