from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include('webpages.urls', namespace='webpages')),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^document/', include('document.urls', namespace='document')),
    url(r'^bid/', include('bid.urls', namespace='bid')),
]
