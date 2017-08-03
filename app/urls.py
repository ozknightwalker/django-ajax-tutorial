from django.conf.urls import include, url
from django.contrib import admin

from poll import urls as poll_urls

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include(poll_urls)),
    url(r'^admin/', include(admin.site.urls)),
]
