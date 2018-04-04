from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^my-files/$', views.MyFiles.as_view(), name='my-files'),
    url(r'^add-file/$', views.AddFile.as_view(), name='add-file'),
    url(r'^edit-file/(?P<pk>[0-9]+)/$', views.EditFile.as_view(), name='edit-file'),
]