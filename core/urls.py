from django.conf.urls import url
from .views import SerialConnenction

urlpatterns = [
    url(r'^serial/$', SerialConnenction.as_view())
]
