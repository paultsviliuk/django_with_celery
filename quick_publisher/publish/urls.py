from django.conf.urls import url
from django.contrib import admin

from publisher.views import view_post

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[a-zA-Z0-9\-]+)', view_post, name='view_post')
]
