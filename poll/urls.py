from __future__ import unicode_literals

from django.conf.urls import url

from poll.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
